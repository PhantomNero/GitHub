import os
from random import shuffle

from flask import *

from db_scripts import get_question_after, get_quises, check_answer


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
    if check_answer(quest_id, answer):
        session['answers'] += 1


def question_form(question):
    answer_list = [
        question[2], question[3], question[4], question[5]
    ]
    shuffle(answer_list)
    return render_template('test.html', question=question[1], question=question[0], answer_list=answer_list)


def quiz_form():
    ''' функция получает список викторин из базы и формирует форму с выпадающим списком'''
    q_list = get_quises()
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
        # тут пока старая версия фуx    нкции:
        if request.method == 'POST':
            save_answers()
        next_question = get_question_after(session['last_question'], session['quiz'])
        if next_question is None or len(next_question) == 0:
            # если мы научили базу возвращать Row или dict, то надо писать не result[o], a result['id']
            return redirect(url_for('result'))
        return question_form(next_question)


def result():
    html = render_template('result.html', right=session['answers'], total=session['total'])
    end_quiz()
    return html


folder = os.getcwd()
# Создаём объект веб-приложения:
app = Flask(__name__, template_folder='folder', static_folder='folder')
app.add_url_rule('/index', 'index', index, methods=['post', 'get'])  # правило для '/index'
app.add_url_rule('/test', 'test', test), methods = ['post', 'get']  # создаёт правило для URL '/test'
app.add_url_rule('/result', 'result', result)  # создаёт правило для URL '/test'
# Устанавливаем ключ шифрования:
app.config['SECRET_KEY'] = 'ThisIsSecretSecretSecretLife'

if __name__ == "__main__":
    # Запускаем веб-сервер:
    app.run()
