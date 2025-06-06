from flask import Flask, render_template, request, redirect, url_for
import subprocess
from Thestatmaker import make_data
import pandas as pd
import sys

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/update', methods=['POST'])
def update_data():
    subprocess.run([sys.executable, 'parser.py'])
    make_data()
    return redirect(url_for('index'))

@app.route('/goalkeepers')
def show_gk():
    return render_template('gk.html', position='Goalkeepers')

@app.route('/defenders')
def show_df():
    return render_template('df.html', position='Defenders')

@app.route('/midfielders')
def show_mf():
    return render_template('mf.html', position='Midfielders')

@app.route('/forwards')
def show_fw():
    return render_template('fw.html', position='Forwards')

if __name__ == '__main__':
    app.run(debug=True)