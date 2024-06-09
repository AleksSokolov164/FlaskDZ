import os  # работа с файловой системой
import sqlite3

from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g
from FDataBase import FDataBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, current_user
from UserLogin import UserLogin

# конфигурационная информация
DATABASE = '/tmp/flsite.db'  # путь
DEBUG = False  # включен реэим отладки
SECRET_KEY = 'akjjjjjjjh79kandck9pAMCKn0lkdcnkj'  # случайный набор для шишрования сессии браузером
#
app = Flask(__name__)
app.config.from_object(__name__)  # загружаем конфигурацию и текущего модуля

app.config.update(dict(DATABASE=os.path.join(app.root_path,
                                             'flsite.db')))  # переопределяем путь. уточняем т.к. одной бд могут пользоваться несколько приложений

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    db = get_db()
    dbase = FDataBase(db)

    print("load_user")
    return UserLogin().fromDB(user_id, dbase)


def connect_db():
    '''устанавливаем соединение с базой данных'''
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
    '''Соединение с базой данных, если его еще нет'''
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    """Закрываем соединение с базой данных, если оно было уставновлено"""
    if hasattr(g, 'link_db'):
        g.link_db.close()


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
    print(f'{current_user.get_id()} ответил неверно')
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
    db = get_db()
    dbase = FDataBase(db)

    if request.method == 'POST':
        if (len(request.form['username']) != 0
                and len(request.form['email']) != 0
                and '@' in request.form['email']
                and request.form['message'] != ''):
            res = dbase.addFeedback(request.form['username'], request.form['email'], request.form['message'])
            if not res:
                flash('Ошибка отправки. Проверьте корректность заполнения полей', category='error')
            else:
                flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки. Проверьте корректность заполнения полей', category='error')

    return render_template('feedback.html', message_menu=dbase.getMenu()), 404


@app.errorhandler(404)
def pageNotFount(error):
    return render_template(('page404.html'))


@app.route('/login', methods=['POST', 'GET'])
def login():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == 'POST':
        user = dbase.getUserByEmail(request.form['email'])
        if user and check_password_hash(user['psw'], request.form['psw']):
            userlogin = UserLogin().create(user)
            login_user(userlogin)
            return redirect(url_for('index'))

        flash('Неверная пара логин\пароль', 'error')
    return render_template('login.html', message_menu=dbase.getMenu())



@app.route('/register', methods=['POST', 'GET'])
def register():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == 'POST':
        if (len(request.form['name']) != 0
                and len(request.form['email']) != 0
                and '@' in request.form['email']
                and request.form['psw'] != ''
                and request.form['psw'] == request.form['psw2']):
            hash1 = generate_password_hash(request.form['psw'])
            res = dbase.addUser(request.form['name'], request.form['email'], hash1)
            if res:
                flash('Вы успешно зарегистрированы', category='success')
                return redirect(url_for('login'))
            else:
                flash('Ошибка  при добавлении в базу данных', category='error')
        else:
            flash('Ошибка. Проверьте корректность заполнения полей', category='error')

    return render_template('register.html', message_menu=dbase.getMenu())


if __name__ == '__main__':
    app.run(debug=True)
