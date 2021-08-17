from bs4 import BeautifulSoup
import requests
res = requests.get('https://quotes.toscrape.com/')
html = res.text
soup = BeautifulSoup(html, 'html.parser')
# print(soup.title.string)
# print(soup.title.parent)
# print(soup.title.parent.name)
# for tag in soup.findAll('a'):
#     print(tag)
with open('bs4quotes.txt', 'w') as f:
    for tag in soup.findAll('span', {'class': 'text'}):
        text = tag.string.replace('“', '').replace('”', '')
        f.write(text)
        f.write('\n')
with open('bs4authors.txt', 'w') as f:
    for tag in soup.findAll('small', {'class': 'author'}):
        f.write(tag.string)
        f.write('\n')
