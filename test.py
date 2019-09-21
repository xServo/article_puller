import requests
url = "https://www.google.com/"
r = requests.get(url)
html = r.text
print(html)
