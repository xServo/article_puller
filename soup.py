from bs4 import BeautifulSoup
import requests
import urllib

with open('sample2.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')



#deletes extra text
filed = soup.find_all("p", attrs={"class":"sr-only c-entry-box--compact__labels-title"})
for i in filed:
    i.decompose()

#prints article and adds quotes around caption
counter = 0
content = soup.find_all("p")
print(soup.h1.text)
for i in content:
    if counter != 0:
        print(i.text, "\n")
    if counter == 0:
        print("\n" + "\"" + i.text + "\"" + "\n")
        counter += 1
