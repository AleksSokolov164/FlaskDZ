from flask import  Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_ARI'] = 'sqlite:///newflask.db'
# db = SQLAlchemy(app)


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('project_info.html')

if __name__ == '__main__':
    app.run(debug=True)