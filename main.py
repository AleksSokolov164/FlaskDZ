import os  # работа с файловой системой
import sqlite3

from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g
from FDataBase import FDataBase
# конфигурационная информация
DATABASE = '/tmp/flsite.db'  # путь
DEBUG = True  # включен реэим отладки
SECRET_KEY = 'akjjjjjjjh79kandck9pAMCKn0lkdcnkj'  # случайный набор для шишрования сессии браузером
#
app = Flask(__name__)
app.config.from_object(__name__)  # загружаем конфигурацию и текущего модуля

app.config.update(dict(DATABASE=os.path.join(app.root_path,
                                             'flsite.db')))  # переопределяем путь. уточняем т.к. одной бд могут пользоваться несколько приложений


# db = SQLAlchemy(app)

# устанавливаем соединение с базой данных
def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row  # записи будут представленны в виде словаря
    return conn


def create_db():
    '''Вспомогательная функция создания таблиц БД'''
    db = connect_db()
    with app.open_resource('sq_db.sql',
                           mode='r') as f:  # прочитали и запустили скрипты по созданию, записали изм, закрыли
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    """ Соединение с базой данных, если его еще нет"""
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route('/index')
@app.route('/')
def index():
    db = get_db()
    return render_template('index.html')


@app.route('/index1')
def index1():
    return render_template('index1.html')


@app.route('/index2')
def index2():
    return render_template('index2.html')


@app.route('/index3')
def index3():
    return render_template('index3.html')


@app.route('/index4')
def index4():
    return render_template('index4.html')


@app.route('/index5')
def index5():
    return render_template('index5.html')


@app.route('/index6')
def index6():
    return render_template('index6.html')


@app.route('/index7')
def index7():
    return render_template('index7.html')


@app.route('/index8')
def index8():
    return render_template('index8.html')


@app.route('/index9')
def index9():
    return render_template('index9.html')


@app.route('/index10')
def index10():
    return render_template('index10.html')


@app.route('/index11')
def index11():
    return render_template('index11.html')


@app.route('/index12')
def index12():
    return render_template('index12.html')


@app.route('/index13')
def index13():
    return render_template('index13.html')


@app.route('/index14')
def index14():
    return render_template('index14.html')


@app.route('/index15')
def index15():
    return render_template('index15.html')


@app.route('/index16')
def index16():
    return render_template('index16.html')


@app.route('/index17')
def index17():
    return render_template('index17.html')


@app.route('/index18')
def index18():
    return render_template('index18.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/project_info')
def project_info():
    return render_template('project_info.html')


@app.route('/feedback', methods=['POST', 'GET'])
def feedback():
    if request.method == 'POST':
        if (len(request.form['username']) != 0
                and len(request.form['email']) != 0
                and '@' in request.form['email']
                and request.form['message'] != ''):
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки. Проверьте корректность заполнения полей', category='error')
    db = get_db()
    dbase = FDataBase(db)
    return render_template('feedback.html', message_menu = dbase.getMenu()), 404


@app.errorhandler(404)
def pageNotFount(error):
    return render_template(('page404.html'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'admin' and request.form['psw'] == '123':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html')


@app.route('/profile/<username>')
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f'Пользователь: {username}'

@app.teardown_appcontext
def close_db(error):
    """Закрываем соединение с базой данных, если оно было уставновлено"""
    if hasattr(g,'link_db'):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)
