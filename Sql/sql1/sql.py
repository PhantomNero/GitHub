from flask import *
#from random import shuffle
#import os
#from db_scripts import get_question_after, get_quises
from db_scripts import get_question_after


def start_quis(quiz_id):
    '''создаёт нужные значения в словаре session'''
    session['quiz'] = quiz_id
    session['last_question'] = 0
    session['answers'] = 0
    session['total'] = []


def end_quiz():
    session.clear()


def save_answers(answer):
    answers = request.form.getlist('answers')
    quest_id = request.form.getlist('answers')
    session['last_question'] = quest_id
    session['total'] += 1
    if check_answers:


def quiz_form():
    ''' функция получает список викторин из базы и формирует форму с выпадающим списком'''
    q_list = get_quisses()
    return render_template('start.html', quiz_list=q_list)


def index():
    ''' Первая страница: если пришли запросом GET, то выбрать викторину,
    если POST - то запомнить id викторины и отправлять на вопросы'''
    if request.method == 'GET':
        # викторина не выбрана, сбрасываем id викторины и показываем форму выбора
        start_quis(-1)
        return quiz_form()
    else:
        # получили дополнительные данные в запросе! Используем их:
        quest_id = request.form.get('quiz')  # выбранный номер викторины
        start_quis(quest_id)
        return redirect(url_for('test'))


def test():
    '''возвращает страницу вопроса'''
    # что если пользователь без выбора викторины пошел сразу на адрес '/test'?
    if not ('quiz' in session) or int(session['quiz']) < 0:
        return redirect(url_for('index'))
    else:
        # тут пока старая версия функции:
        result = get_question_after(session['last_question'], session['quiz'])
        if result is None or len(result) == 0:
            return redirect(url_for('result'))
        else:
            session['last_question'] = result[0]
            # если мы научили базу возвращать Row или dict, то надо писать не result[0], а result['id']
            return '<h1>' + str(session['quiz']) + '<br>' + str(result) + '</h1>'


def result():
    end_quiz()
    return "that's all folks!"


# Создаём объект веб-приложения:
app = Flask(__name__)
app.add_url_rule('/', 'index', index)  # создаёт правило для URL '/'
app.add_url_rule('/index', 'index', index, methods=['post', 'get'])  # правило для '/index'
app.add_url_rule('/test', 'test', test)  # создаёт правило для URL '/test'
app.add_url_rule('/result', 'result', result)  # создаёт правило для URL '/test'
# Устанавливаем ключ шифрования:
app.config['SECRET_KEY'] = 'ThisIsSecretSecretSecretLife'

if __name__ == "__main__":
    # Запускаем веб-сервер:
    app.run()
