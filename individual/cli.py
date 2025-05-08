#cli.py
#Anthony Iyengunmwena
#4/17/25

#NAME: cli.py - command-line interface exercise

#SYNOPSIS: python3 cli.py by Anthony Iyengunmwena

#DESCRIPTION: Shows a list of the titles of all the movies with the action genre/type

import csv
import argparse


...

def searchByGenre(findGenre):
    with open('../data/tmdb_5000_movies.csv') as f:
        reader = csv.reader(f)
        for movie_row in reader:
            genreList =movie_row[1]
            if findGenre.lower() in genreList.lower():
                print(movie_row[6])


def main():
    parser = argparse.ArgumentParser(description='Search dataset by genres.')
    parser.add_argument('genre',help='Genre your searching for')
    parsed_arguments = parser.parse_args()
    searchByGenre(parsed_arguments.genre)

if __name__ == '__main__':
    main()

