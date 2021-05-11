from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pandas as pd
import recommendation

app = Flask(__name__)
CORS(app)

def get_data():
    data = pd.read_csv('dataset/movie_data.csv')
    return data

@app.route('/')
def homepage():
    data = get_data()
    original_title = data.original_title
    return render_template('form.html', movie_list=original_title)

@app.route('/movie', methods=['GET', 'POST'])
def recommend_movies():
    if request.method == 'POST':
        # res = recommendation.results(request.args.get('title'))
        # res = recommendation.results(request.form.value)
        # print(res)
        res = recommendation.results(request.form.get('title'))
        return render_template('/index.html', list=res)
    # res = recommendation.results(request.args.get('title'))
    # return render_template('/index.html', list=res)

if __name__ == '__main__':
    app.run(port=5000, debug = True)
