from flask import  Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_ARI'] = 'sqlite:///newflask.db'
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
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/project_info')
def project_info():
    return render_template('project_info.html')

if __name__ == '__main__':
    app.run(debug=True)