from bs4 import BeautifulSoup
import requests
import urllib

file_name = input("Please enter a name for your file\n")
out = open(file_name + ".txt", "a") 

with open('sample.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')



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
