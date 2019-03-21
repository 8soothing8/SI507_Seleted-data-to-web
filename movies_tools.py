
# -*- coding: utf-8 -*-
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

import datetime
import random
import csv
import numpy as np
from itertools import product, permutations, islice

# Open the file and convert it to a list
with open('movies_clean.csv', 'r', encoding = 'utf8') as movies_source:
    movies_data = csv.reader(movies_source, delimiter=',')
    movies_list = list(movies_data)

# Creating the movie instances and formatize them
class Movie:
    def __init__(self, title, rate):
        self.title = title
        self.rate = rate
    def __str__(self):
        return "{} | {}".format(self.title, self.rate)

#def make_movie_instances(list_of_movies):
	# Use a raw for loop to populate the list of Movie instances
movie_instances_list = []
for movie in movies_list:
    for a in movie:
        a_title = movie[0]
        a_rate = movie[6]
    movie_instances_list.append(Movie(a_title, a_rate))
#    return movie_instances_lists

if __name__ == "__main__":
#    my_movie_objects = list(make_movie_instances(movies_list))
    print(movie_instances_list)
