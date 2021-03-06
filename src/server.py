#!/usr/bin/python

'''
File: server.py

Server management for the data analytics portion of Spinosaurus
'''

from json import load

from flask import Flask, render_template, request
from reader.tacocat import Tacocat

app = Flask(__name__)


@app.route('/')
def home():

    return render_template('home.html')


# This file has a button to begin the processes required
# for beginning serialiazation
@app.route('/play')
def play():

    tacocat_obj = Tacocat()

    tacocat_obj.racecar()

    return render_template('play.html')


# Transform to get_info
# /sloth provides a graph that provides data reading on a person's positioning
@app.route('/success', methods=['GET', 'POST'])
def get_info():

    if request.method == 'GET':
        with open('data.json') as data_file:
            data = load(data_file)

        return render_template('success.html', data=data)


@app.route('/sloth')
def sloth():
    return render_template('sloth.html')


# ----------------------------- main ----------------------------- #

if __name__ == "__main__":
    app.run(debug=True)
