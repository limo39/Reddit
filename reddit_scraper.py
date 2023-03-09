import requests
from bs4 import BeautifulSoup

url = 'https://www.reddit.com/r/Python/hot/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

post_titles = soup.find_all('h3', {'class': '_eYtD2XCVieq6emjKBH3m'})

for title in post_titles:
    print(title.text)

post_links = soup.find_all('a', {'class': 'SQnoC3ObvgnGjWt90zD9Z'})

for link in post_links:
    print(link['href'])
