from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import recommendation

app = Flask(__name__)
CORS(app)

@app.route('/')
def homepage():
    return render_template('form.html')

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
