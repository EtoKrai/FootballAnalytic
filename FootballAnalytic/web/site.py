from flask import Flask, render_template, request, redirect, url_for
import subprocess
import pandas as pd
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from rating_maker import make_data



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/update', methods=['POST'])
def update_data():
    subprocess.run([sys.executable, 'data/parser.py'])
    make_data()
    return redirect(url_for('index'))

def load_and_sort_table(position, sort='Rating', ascending=False):
    file_path = f"web/templates/tables/{position}.csv"
    df = pd.read_csv(file_path)
    if sort in df.columns:
        df = df.sort_values(by=sort, ascending=ascending)
    return df

@app.route('/goalkeepers')
def show_gk():
    sort = request.args.get('sort', 'Rating')
    ascending = request.args.get('ascending', 'false') == 'true'
    gk_df = load_and_sort_table('gk', sort, ascending)
    return render_template('gk.html',
                         position='Вратари',
                         players=gk_df.to_dict('records'),
                         sort=sort,
                         ascending=ascending)

@app.route('/defenders')
def show_df():
    sort = request.args.get('sort', 'Rating')
    ascending = request.args.get('ascending', 'false') == 'true'
    df_df = load_and_sort_table('df', sort, ascending)
    return render_template('df.html',
                         position='Защитники',
                         players=df_df.to_dict('records'),
                         sort=sort,
                         ascending=ascending)

@app.route('/midfielders')
def show_mf():
    sort = request.args.get('sort', 'Rating')
    ascending = request.args.get('ascending', 'false') == 'true'
    mf_df = load_and_sort_table('mf', sort, ascending)
    return render_template('mf.html',
                         position='Полузащитники',
                         players=mf_df.to_dict('records'),
                         sort=sort,
                         ascending=ascending)

@app.route('/forwards')
def show_fw():
    sort = request.args.get('sort', 'Rating')
    ascending = request.args.get('ascending', 'false') == 'true'
    fw_df = load_and_sort_table('fw', sort, ascending)
    return render_template('fw.html',
                         position='Нападающие',
                         players=fw_df.to_dict('records'),
                         sort=sort,
                         ascending=ascending)

if __name__ == '__main__':
    app.run(debug=True)