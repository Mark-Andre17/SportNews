import requests
from bs4 import BeautifulSoup

serch_question = input('Что вы хотите найти на спорт-экспресс: ')
serch = [serch_question]
url = 'https://www.sport-express.ru/news/'
response = requests.get(url)
response.raise_for_status()
req = response.text


def parsing_SE():
    soup = BeautifulSoup(req, 'html.parser')
    articles = soup.find_all('div', class_='se19-news-column2')
    for article in articles:
        headers = article.find('a', class_='se19-news-item__link').text
        time = article.find('div', class_='se19-news-item__info mt_10 se19-news-item__dot fs_13 lh_14').text
        preview_text = article.text
        link = article.find('a', class_='se19-news-item__link').get('href')

        for a in serch:
            if (a.lower() in headers.lower()) or (a.lower() in preview_text.lower()):
                print(f'Время:{time}Заголовок:{headers}Ссылка:{link}')


if __name__ == '__main__':
    parsing_SE()
