from bs4 import BeautifulSoup
import requests
import urllib

#goes through links
url_list = []
links = open("./url_list", "r")
line = links.readline()
while line:
    url_list.append(line.strip())
    line = links.readline()

links.close()

cnt = 1
for i in url_list:
    file_name = "article" + str(cnt)
    url = i
    cnt += 1    

    new_url = requests.get(url)
    html = new_url.text

    out = open("./articles/" + file_name + ".txt", "a") 
    soup = BeautifulSoup(html, 'lxml')

    #deletes extra text
    filed = soup.find_all("p", attrs={"class":"sr-only c-entry-box--compact__labels-title"})
    for i in filed:
        i.decompose()

    #prints article and adds quotes around caption
    counter = 0
    content = soup.find_all("p")
    out.write(str(soup.h1.text))
    out.write("\n")
    for i in content:
        if counter != 0:
            out.write(str(i.text))
            out.write("\n\n")
        if counter == 0:
            out.write("\"" + str(i.text) + "\"")
            out.write("\n\n\n\n")
            counter += 1
out.close()
