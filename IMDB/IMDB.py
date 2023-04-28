from bs4 import BeautifulSoup
import requests
import pandas as pd

try:
    url = 'https://www.imdb.com/chart/top/'
    source = requests.get(url)
    source.raise_for_status()
    soup = BeautifulSoup(source.text, 'html.parser')
    movies = soup.find('tbody', class_="lister-list").find_all('tr')
    data = []
    for movie in movies:
        name = movie.find('td', class_='titleColumn').a.text
        rank = movie.find('td', class_='titleColumn').get_text().strip().split('.')[0]
        year = movie.find('td', class_='titleColumn').span.text.strip('()')
        rating = movie.find('td', class_='ratingColumn imdbRating').strong.text
        Director = movie.find('td', class_='titleColumn').a['title'].split('(dir.),')[0].strip()
        Actors = movie.find('td', class_='titleColumn').a['title'].split('(dir.),')[1].strip()
        users_text = movie.find('td', class_='ratingColumn imdbRating').strong['title']
        Users_count = int(users_text.split()[3].replace(',', ''))
        data.append([rank, name, year, rating, Users_count, Director, Actors])

    movies_df = pd.DataFrame(data, columns=['Rank', 'Name', 'Year', 'Rating', 'Users_count', 'Director', 'Actors'])
    movies_df.to_excel('IMDB_movies.xlsx', index=False)
except Exception as e:
    print(f'Error occurred while processing URL {url}: {e}')
movies_df