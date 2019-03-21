# SI507_pjt2

You should make clear what this program can do and explain exactly how to run the Flask app, down to what to type in to your command prompt. Please use markdown syntax to make your text clear and well-organized.

## What it does

This program can show 1) all movies in the list, 2) the number of movies in the list, 3) and the ratings of five random movies in the list. When you run the file 'SI507_project2.py', it connects the codes in the file 'movies_tools.py' that opens the movie list csv file and generate a list of instances of movies. The file 'SI507_project2.py' shuffles the list and take 5 random movies out of it.     

## How to run

First, put 'movies_clean.csv', 'SI507_project2.py' and 'movies_tools.py' files all together in the same directory. Then, run the 'SI507_project2.py' file on your command.

To get results of this program, you need to type the routes below on your browser.

The first page of the local host URL http://localhost:5000/ will display an introduction message to a user. 

The route http://localhost:5000/movies/<number> will give the number of movies recorded in the 'movies_clean.csv' file. A user can replace <number> with any words.

Lastly, the URL http://localhost:5000/movies/ratings will suggest five different movies with their ratings.
