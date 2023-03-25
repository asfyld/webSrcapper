import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top/'

headers = {"Accept-Language": "en-US, en;q=0.5"}

print('Downloading page %s ...' % url)

response = requests.get(url, headers=headers)
html_content = response.content

print('The page has been successfully downloaded.')

print('Parsing the page...')

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', {'class': 'chart'})

movies = []
for row in table.find_all('tr')[1:251]:
    title_column = row.find('td', {'class': 'titleColumn'})
    title = title_column.a.text
    year = title_column.span.text
    rating = row.find('td', {'class': 'ratingColumn imdbRating'}).text.strip()
    movies.append((title, year, rating))

print('The page has been parsed successfully.')

f = open('top250movies.txt', 'w')

for i, movie in enumerate(movies, start=1):
    f.write(f'{i}. {movie[0]} {movie[1]} - {movie[2]}\n')
f.close()

print('The movie list is successfully written in %s file!' %f.name)
