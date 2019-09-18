from bs4 import BeautifulSoup
import requests
import urllib

with open('sample.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

title = soup.title.string
caption = soup.h2.string
body = soup.p.string

print(title)
print(caption)

table = soup.find_all('div',attrs={"class":"body"})
for x in table:
    print(x.find('p'))
