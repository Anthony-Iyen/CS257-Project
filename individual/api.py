'''
    Api.py
    Anthony Iyengunmwena,Jeff Ondich 23 April 2025
    Last updated 23 April 2025

    A flask and API endpoints assignment modifing my projects dataset.

    Note: some code reused from teacher example.
'''

import sys
import argparse
import flask
import json
import csv

app = flask.Flask(__name__)


'''def searchByGenre(findGenre):#
    with open('../data/tmdb_5000_movies.csv') as f:
        reader = csv.reader(f)
        for movie_row in reader:
            genreList =movie_row[1]
            if findGenre.lower() in genreList.lower():
                print(movie_row[6])

'''

@app.route('/')
def hello():
    return 'Hello, Citizen of CS257. This is revised version of flask_sample.py to fit my work'



@app.route('/genre/<findGenre>')
def search_by_genre(findGenre):
    '''Returns the list of movies that match the given genre
    '''
    movie_dictionary = []
    with open('../data/tmdb_5000_movies.csv') as f:
        lower_genre_name = findGenre.lower()
        reader = csv.DictReader(f)
        for movie_row in reader:
            genreList =movie_row['genres']
            if findGenre.lower() in genreList.lower():
                movie_dictionary.append(movie_row['title'])

    return json.dumps(movie_dictionary)





@app.route('/help')
def get_help():
    return flask.render_template('help.html')





if __name__ == '__main__':
    parser = argparse.ArgumentParser('A sample Flask application/API')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)
