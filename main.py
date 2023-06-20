from flask import Flask, render_template, jsonify, request, session, redirect, url_for, g
import os
from database import *

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/', methods=['POST','GET'])
def userlogin():

  if request.method == 'POST':
    session.pop('user',None)

    if check_ulogin(request.form['uname'],request.form['upass']):
      session['user'] = request.form['uname']
      return redirect(url_for('udashboard'))
    
  return render_template('userlogin.html')

@app.route("/dashboard")
def udashboard():
    if g.user:
      adetails = acc_details(session['user'])
      bdetails = branch_details(adetails[0][6])
      return render_template('udashboard.html',adetails=adetails,bdetails=bdetails)
    else:
       return redirect(url_for('userlogin'))
       

@app.route('/admin')
def emplogin():
    return render_template('emplogin.html')

@app.route('/acc', methods=['post'])
def accounts():
    # data = request.args
    data = request.form
    return jsonify(data)

@app.before_request
def before_request():
  g.user = None
  if 'user' in session:
    g.user = session['user']

@app.route('/dropsession')
def dropsession():
  session.pop('user',None )
  return redirect(url_for('login'))

app.run(debug=True)