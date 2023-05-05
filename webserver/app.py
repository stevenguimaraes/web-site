from flask import Flask, render_template
from templates.rev  import rev
import os
import subprocess


app = Flask(__name__ , static_folder='./templates/img')

@app.route('/')
def home():
    return render_template('index.html',)



if __name__ == '__main__':
    rev()
    app.run(debug=True)
