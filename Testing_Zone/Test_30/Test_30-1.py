#! /usr/bin/python

from flask import Flask, render_template

menu = ["Первый", "Второй", "Третий"]

app = Flask(__name__)


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html', title='Про Flask', menu=menu)





@app.route('/about')
def about():
    return render_template('about.html', title='О сайте')


@app.route('/help')
def help():
    return render_template('help.html', title='Помощь')

@app.route('/hobbi')
def hobbi():
    return render_template('hobbi.html', title='Хобби')


if __name__ == "__main__":
    app.run(debug=True)
