import sqlite3

db_name = 'quiz.sqlite'
conn = None
cursor = None


def open_db():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()


def close():
    cursor.close()
    conn.commit()


def do(query):
    cursor.execute(query)
    conn.commit()


def create():
    open_db()
    cursor.execute('PRAGMA foreign_keys=on')

    do('''CREATE TABLE IF NOT EXISTS quiz
    (id INTEGER PRIMARY KEY, name VARCHAR)''')

    do('''CREATE TABLE IF NOT EXISTS question(
        id INTEGER PRIMARY KEY,
        question VARCHAR,
        answer VARCHAR,
        wrong1 VARCHAR,
        wrong2 VARCHAR,
        wrong3 VARCHAR)''')

    do('''CREATE TABLE IF NOT EXISTS quiz_content(
        id INTEGER PRIMARY KEY,
        quiz_id INTEGER,
        question_id INTEGER,
        FOREIGN KEY(quiz_id) REFERENCES quiz(id),
        FOREIGN KEY(question_id) REFERENCES question(id))''')

    close()


def clear_db():
    open_db()
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    query = '''DROP TABLE IF EXISTS question'''
    do(query)
    close()


def add_questions():
    questions = [
        ('Сколько месяцев в году имеют 28 дней?', 'Все', 'Один', 'Ни одного', 'Два'),
        ('Чему равно число Пи?', 'Примерно 3.14', '3', '10', 'Ровно 3.14'),
        ('Что больше слона и ничего не весит?', 'Тень слона', 'Воздушный шар', 'Аэростат', 'Кит'),
        ('Сколько секунд в километре?', 'Нисколько', '160', '100', 'Мало'),
        ('Кто автор 3-го закона Ньютона?', 'Ньютон', 'Конфуций', 'Пифагор', 'Архимед'),
        ('Какой рукой лучше размешивать чай?', 'Ложкой', 'Левой', 'Правой', 'Кружкой'),
        ('Что не имеет длины, глубины, ширины, высоты, но можно измерить?', 'Время', 'Воздух', 'Вода', 'Глупость')
    ]
    open_db()
    cursor.executemany(
        '''INSERT INTO question (question, answer, wrong1, wrong2 , wrong3) VALUES (?, ?, ?, ?, ?)''',
        questions
    )
    conn.commit()
    close()


def add_quiz():
    quizes = [
        ('Своя игра',),
        ('Кто хочет стать миллионером?',),
        ('Самый умный',)
    ]
    open_db()
    cursor.executemany('''INSERT INTO quiz (name) VALUES (?)''', quizes)
    conn.commit()
    close()


def add_links():
    open_db()
    cursor.execute('''PRAGMA foreign_keys=on''')
    query = 'INSERT INTO quiz_content (quiz_id, question_id) VALUES (?, ?)'
    answer = input('Добавить связь (у/n)?')
    while answer != 'n':
        quiz_id = int(input('id викторины:'))
        question_id = int(input('id вопроса:'))
        cursor.execute(query, [quiz_id, question_id])
        conn.commit()
        answer = input('Добавить связь (у/n)?')
    close()


def get_question_after(question_id=0, quiz_id=1):
    open_db()
    query = '''
    SELECT quiz_content.id, question.question, question.answer,
    question.wrong1, question.wrong2, question.wrong3
    FROM question, quiz_content
    WHERE quiz_content.id > ? AND quiz_content.quiz_id = ?
    AND question.id = quiz_content.question_id
    ORDER BY quiz_content.id
    '''
    cursor.execute(query, [question_id, quiz_id])
    result = cursor.fetchone()
    close()
    return result


def show_tables():
    open_db()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print("Tables in the database:")
    for table in tables:
        print(table[0])
    close()


def main():
    clear_db()
    create()
    add_questions()
    add_quiz()
    add_links()
    show_tables()
    print(get_question_after(3, 1))


if __name__ == '__main__':
    main()