import requests
from bs4 import BeautifulSoup
import json


def articles():
    url = 'https://habr.com/ru/feed/'
    headers = {
        'User-Agent': 'user_agent'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles_dict = {}
    article_counter = 0
    try:
        all_hrefs_articles = soup.find_all('a', attrs={'class': "tm-title__link"})
        for article in all_hrefs_articles:
            article_name = article.find('span').text
            article_link = f'https://habr.com{article.get("href")}'
            articles_dict[article_name] = article_link
            article_counter += 1
            if article_counter == 10:
                break
        return articles_dict
    except Exception as e:
        print(e)
        return None


def articles_by_flows(flow):
    url = f'https://habr.com/ru/flows/{str(flow)}/articles/'
    headers = {
        'User-Agent': 'user_agent'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles_dict = {}
    article_counter = 0
    try:
        all_hrefs_articles = soup.find_all('a', attrs={'class': "tm-title__link"})
        for article in all_hrefs_articles:
            article_name = article.find('span').text
            article_link = f'https://habr.com{article.get("href")}'
            articles_dict[article_name] = article_link
            article_counter += 1
            if article_counter == 10:
                break
        return articles_dict
    except Exception as e:
        print(e)
        return None


def complaint(client, text):
    with open('complaints.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    client_data = data.get(str(client), {})

    client_data[len(client_data) + 1] = str(text)

    data[str(client)] = client_data

    with open('complaints.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

