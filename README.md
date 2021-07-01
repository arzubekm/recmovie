# movierec
Movie Recommendation system (movierec) project is built using [Flask](http://flask.pocoo.org/). It is a simple movie recommendation application that will show similar movies to your input.

The application model uses **Content Based Recommendations** to find similar movies based on [Kaggle](https://www.kaggle.com/tmdb/tmdb-movie-metadata) dataset.

## Setup
### Install and initialize virtual environment
```
pip install virtualenv
python -m venv env
source env/bin/activate
```
### Install required libraries
```
pip install -r requirements.txt
```
### Clone the project
```
git clone https://github.com/arzubekm/recmovie.git
```
### Run the app
```
cd recmovie
export FLASK_APP=app.py
flask run
```
### Access the app
You can open the app in your browser by typing http://127.0.0.1:5000/

Also, it is hosted on Heroku [https://recmovie-api.herokuapp.com](https://recmovie-api.herokuapp.com/)
