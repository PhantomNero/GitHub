from db_scripts import *
from flask import *

def index():
    max_quiz = 3
    session["quiz" = randint(1, max_quiz)]
    session[last_question] = 0
    return '<a href="/test">Тест</a>'
def test():
    result = get_question_after(session['last_question'], session['quiz'])
def result():

# создаём объект веб-приложения
app = Flask(__name__)
app.add_url_rule('/', 'index', index)  # создаёт правило для URL '/'
app.add_url_rule('/test', 'test', test)  # создаёт правило для URL !/test!
app.add_url_rule('/result', 'result', result)  # создаёт правило для URL '/result'
