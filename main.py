from flask import Flask, render_template, jsonify, request
from database import *

app = Flask(__name__)

print(load_student(dept='phy'))

# @app.route("/")
# def index():
#     return render_template('index.html',query=load_faculty())

@app.route("/dashboard")
def student():
    return render_template('dashboard.html')

# @app.route("/student")
# def student():
#     return render_template('student.html', quer=load_student(dept='phy'))

@app.route('/')
def new_accounts():
    return render_template('login.html')

@app.route('/acc', methods=['post'])
def accounts():
    # data = request.args
    data = request.form
    return jsonify(data)

app.run(debug=True)