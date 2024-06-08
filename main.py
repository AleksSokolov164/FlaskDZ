from flask import Flask, render_template, url_for, request, flash, session, redirect, abort
from flask_sqlalchemy import SQLAlchemy

#
app = Flask(__name__)
app.config['SECRET_KEY'] = 'akjjjjjjjh79kandck9pAMCKn0lkdcnkj'


# db = SQLAlchemy(app)


@app.route('/index')
@app.route('/')
def index():
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
        print(request.form)
    return render_template('feedback.html'), 404


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

if __name__ == '__main__':
    app.run(debug=True)
