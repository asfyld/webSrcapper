import requests
from bs4 import BeautifulSoup

# Define the IMDb URL for the top 250 movies
url = 'https://www.imdb.com/chart/top/'

# Set the English language
headers = {"Accept-Language": "en-US, en;q=0.5"}

# Inform the user about download progress
print('Downloading page %s ...' % url)

# Send a GET request to the URL and get the HTML content
response = requests.get(url, headers=headers)
html_content = response.content

# Inform the user about download progress
print('The page has been successfully downloaded.')

# Inform the user about parsing progress
print('Parsing the page...')

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the table containing the top 250 movies
table = soup.find('table', {'class': 'chart'})

# Extract the movie titles and ratings from the table
movies = []
for row in table.find_all('tr')[1:251]: # get first 250 rows
    title_column = row.find('td', {'class': 'titleColumn'})
    title = title_column.a.text
    year = title_column.span.text
    rating = row.find('td', {'class': 'ratingColumn imdbRating'}).text.strip()
    movies.append((title, year, rating))

# Inform the user about parsing progress
print('The page has been parsed successfully.')

# Save the list of movies to a txt file
f = open('top250movies.txt', 'w')

for i, movie in enumerate(movies, start=1):
    f.write(f'{i}. {movie[0]} {movie[1]} - {movie[2]}\n')
f.close()

# Inform the user about file writing progress
print('The movie list is successfully written in %s file!' %f.name)