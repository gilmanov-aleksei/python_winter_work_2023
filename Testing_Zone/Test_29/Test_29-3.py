#! /usr/bin/python

from flask import Flask, render_template

manu = ["Первый", "Второй", "Третий"]

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def index(menu=None):
    return render_template('index.html', title='Про Flask', menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', title='О сайте')


if __name__ == "__main__":
    app.run(debug=True)
