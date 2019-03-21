
from flask import Flask, render_template
from movies_tools import *
from random import sample as movie_sampler
import random


# Set up application
app = Flask(__name__)

# Routes

@app.route('/')
def start():
    return '<h1> Hey, do you want to see my movie recommendations? <h1>'

@app.route('/movies/<number>')
def movies_count(number):

    with open('movies_clean.csv', 'r', encoding = 'utf8') as movies_source:
        movies = csv.reader(movies_source, delimiter=',')
        number = sum(1 for lines in movies) - 1
        return '<h1> {} movies are recorded <h1>'.format(number)

@app.route('/movies/ratings')
def movie_rating():
    random.shuffle(movie_instances_list)
    # print(movie_instances_list)
    instance_pick1 = movie_instances_list[0]
    instance_pick2 = movie_instances_list[1]
    instance_pick3 = movie_instances_list[2]
    instance_pick4 = movie_instances_list[3]
    instance_pick5 = movie_instances_list[4]
    return "<h1> {} <br> {} <br> {} <br> {} <br> {} <h1>".format(instance_pick1.__str__(),instance_pick2.__str__(),instance_pick3.__str__(),instance_pick4.__str__(),instance_pick5.__str__())

if __name__ == '__main__':
    app.run(debug=True)
