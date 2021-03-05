import os
import requests
import pprint
import pandas as pd


BASE_DIR = os.path.dirname(__file__)
api_key = '9221487f2fa15bc99d98276813a19d25'
api_key_v4 = ('eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5MjIxNDg3ZjJmYTE1YmM5OWQ5ODI3Nj'
    'gxM2ExOWQyNSIsInN1YiI6IjYwM2U4YThlZmNhZGI0MDAyYThiZTI1NSIsInNjb3BlcyI6WyJ'
    'hcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.v0NT2FAB-NyffVMC7GOvTZ-Z6zUux5cGtsleKQZfS'
    '_Q')


'''
Endpoint
GET
/movie/{movie_id}
https://api.themoviedb.org/3/movie/550?api_key=9221487f2fa15bc99d98276813a19d25
'''

# Version 3
# api_version = 3
# api_base_url = f'https://api.themoviedb.org/{api_version}'
# movie_id = 500
# endpoint_path = f'/movie/{movie_id}'
# endpoint = f'{api_base_url}{endpoint_path}'
# # r = requests.get(endpoint, data={'api_key': api_key})
# r = requests.get(f'{endpoint}?api_key={api_key}')

# Version 4
# api_version = 4
# api_base_url = f'https://api.themoviedb.org/{api_version}'
# movie_id = 501
# endpoint_path = f'/movie/{movie_id}'
# endpoint = f'{api_base_url}{endpoint_path}/'
# headers = {
#     'Authorization': f'Bearer {api_key_v4}',
#     'Content-Type': 'application/json;charset=utf-8'
# }
# r = requests.get(endpoint, headers=headers)
# print(r.status_code)
# print(r.text)


def search_movie(base_url, api_key, api_version=3, movie_query=''):
    '''Return movie results based on movie_query
    Endpoint
    GET
    /search/movie
    https://api.themoviedb.org/3/search/movie
        ?api_key=9221487f2fa15bc99d98276813a19d25
        &query=spiderman
    '''
    api_base_url = f'{base_url}/{api_version}'
    endpoint_path = '/search/movie'
    endpoint = f'{api_base_url}{endpoint_path}'
    r = requests.get(f'{endpoint}?api_key={api_key}&query={movie_query}')
    if r.status_code == 200:
        return r.json()
    else:
        return f'encountered {r.status_code} error'


def list_id_movie(results):
    movies = results['results']
    for movie in movies:
        # print(f'{movie["id"]}: {movie["title"]}')
        print(movie)


def save_to_csv(results, movie_query):
    movies = results['results']
    movie_data = []
    output = f'{movie_query}.csv'
    for movie in movies:
        movie_data.append(movie)
    df = pd.DataFrame(movie_data)
    print(df.head())
    csv_fpath = os.path.join(BASE_DIR, output)
    df.to_csv(csv_fpath, index=False)


# Search Movie version 3
base_url = 'https://api.themoviedb.org'
api_version = 3
movie_query = 'matrix'
results = search_movie(base_url, api_key, api_version, movie_query)
# pprint.pprint(results)
# list_id_movie(results)
save_to_csv(results, movie_query)


