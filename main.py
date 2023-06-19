from flask import Flask, render_template, jsonify, request
from sqlalchemy import create_engine, text

app = Flask(__name__)

engine = create_engine("mysql://root:ubuntu@localhost/university",echo = True)

def load_faculty():
    with engine.connect() as conn:
        result = conn.execute(text("select * from faculty"))
        return result.all()
    
def load_student():
    with engine.connect() as conn:
        result = conn.execute(text("select * from students"))
        return result.all()

def load_student(dept):
    with engine.connect() as conn:
        result = conn.execute(text("select * from students where dept = :val"),val=dept)
        return result.all()


print(load_student(dept='phy'))

@app.route("/")
def index():
    return render_template('index.html',query=load_faculty())

@app.route("/student")
def student():
    return render_template('student.html', quer=load_student(dept='phy'))

@app.route('/newacc')
def new_accounts():
    return render_template('account.html')

@app.route('/acc', methods=['post'])
def accounts():
    # data = request.args
    data = request.form
    return jsonify(data)

app.run(debug=True)