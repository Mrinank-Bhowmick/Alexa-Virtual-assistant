import requests

def news(query):
    url = "https://newsapi.org/v2/top-headlines?country=in"
    response = requests.get(url)
    data = response.json()
    news = data['articles']
    result = []
    for i in range(0, len(news)):
        result.append(news[i]['title'])
    return result