from bs4 import BeautifulSoup
import urllib.request

req = urllib.request.urlopen('https://www.newsvl.ru/')
html = req.read()

soup = BeautifulSoup(html, 'html.parser')
news = soup.find_all('li', class_='story-list__item')
results = []

for item in news:
    title = item.find('a', title_='').get_text(strip=True)
    href = item.a.get('href')
    results.append({
        'title': title,
        'href': href
    })

f = open('news.txt', 'w', encoding='utf-8')
i = 1
for item in results:
    f.write(f'Новость № {i}\n\nНазвание: {item["title"]}\nСсылка:{item["href"]}\n\n*********************\n')
    i += 1
f.close()
