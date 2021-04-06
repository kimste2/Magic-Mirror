from flask import render_template
from app import app
from app.forms import LoginForm
import sys
sys.path.insert(1, "/home/pi/Documents/microblog/supportScripts/")
import weather
import swanson
import trivia 
@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    user = {'username' : 'kimste2' }
    posts = [
        {
            'author': "swanson", 
            'body': swanson.get1Quote()
        },
        {
            'author': "weather",  
            'body' : weather.getWeather()
        },
        {   'author': "triviaQuesiton",  
            'body' : trivia.getQuestion()
        },
        {
            'author': "triviaResponses", 
            'body' : trivia.getAnswers()
        }
    ]

    return render_template('index.html',title="Home", user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
