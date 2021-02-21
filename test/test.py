""" I import flask because I will use this for my web application,
    I import render_template because this is a function that will pull out my html
    I import json to read and load my database which is a json file
    I import random so I can generate random numbers which links to my questions."""
from flask import Flask , render_template , request, redirect, url_for
import json
import os
from random import randrange


# I will be using python flask to create this program
app = Flask(__name__)
# This opens my json database which is located in the static folder
# The variable database_json  is equal to a list where each line is equal to item
# So all of my data for each question is in this variable
with open(os.path.join('static', 'database.json'), 'r') as f:
    database_json = f.readlines()


# Enumerate function assigns a number value to each item in the list
# This turns my json file into a python dictionary while getting rid of the \n.
for i, line in enumerate(database_json):
    database_json[i] = json.loads(line.replace('\n', ''))



def random_generate():
    """this function gives me two lists, one with random numbers between 0-49
     and the other with the questions that are associated with those numbers."""
    global questions
    questions = []
    random_nums = []
    while True:
        number = randrange(50)
        if number not in random_nums:
            random_nums.append(number)
        if len(random_nums) == 5:
                break
    questions = [database_json[i] for i in random_nums]



# this is where the quiz will be generated, with test.html being run.
@app.route('/')
@app.route('/home')
def home():
    """This is endpoint for my quiz generation."""
    random_generate()
    return render_template("test.html", questions = enumerate(questions))

# this is where the quiz scores will be generated. I add the score by 1 every
# time that the form answer is equal to the answer in my json file. the zip function
# creates a tuple with my question and answer value.
# the NameError is simply put because if an error is to pop up, the progroam will
# return to the /home screen.


@app.route('/score', methods=['POST'])



def score():
    """This is the endpoint for the quiz score generation."""
    try:
        answers = request.form
        score = 0
        for i, answer in answers.items():
            if answer.lower() == questions[int(i)]['a'].lower():
                score += 1

        return render_template("score.html", score=score, solutions=zip(questions, answers.values()))
    except NameError:
        return redirect(url_for('home'))

# this is what runs the program.
if __name__ == "__main__":
    app.debug = True
    app.run(threaded=True)
