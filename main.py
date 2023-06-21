from flask import Flask, render_template, jsonify, request, session, redirect, url_for, g
import os
from database import *
import json

app = Flask(__name__)
app.secret_key = os.urandom(24)

# User Login Page

@app.route('/', methods=['POST','GET'])
def userlogin():
  if request.method == 'POST':
    session.pop('user',None)

    if request.form['acc_type'] == 'Customer' and check_ulogin(request.form['uname'],request.form['upass']):
      session['user'] = request.form['uname']
      return redirect(url_for('udashboard'))
    
    elif request.form['acc_type'] == 'Employee' and check_elogin(request.form['uname'],request.form['upass']):
      session['user'] = request.form['uname']
      return redirect(url_for('edashboard'))
    
  return render_template('userlogin.html')

# User Dashboard
@app.route("/dashboard")
def udashboard():
    if g.user:
      adetails = acc_details(session['user'])
      bdetails = branch_details(adetails[0][6])
      trdetails = acc_tranaction(session['user'])
      return render_template('udashboard.html',adetails=adetails,bdetails=bdetails,trdetails=trdetails)
    else:
       return redirect(url_for('userlogin'))
    
@app.route("/employee")
def edashboard():
  if g.user:
    emp_det, br_detail = acc_emp(session['user'])
    tr_detail = all_tr()
    return render_template('edashboard.html',emp_det=emp_det, br_detail=br_detail, tr_detail=tr_detail)
  else:
    return redirect(url_for('userlogin')) 
       
 
# Account Opening Form
@app.route('/newacc',methods=['POST','GET'])
def accounts():
  if g.user:
    return render_template('accopen.html')
  else:
    return redirect(url_for('userlogin'))


# 
@app.route('/transaction',methods=['POST','GET'])
def utranaction():
  return render_template('utransaction.html')

@app.route('/deposit',methods=['POST','GET'])
def deposit():
  return render_template('deposit.html')



@app.route('/data', methods=['GET','POST'])
def data():
  return jsonify(request.form)




@app.before_request
def before_request():
  g.user = None
  if 'user' in session:
    g.user = session['user']

@app.route('/dropsession')
def dropsession():
  session.pop('user',None )
  return redirect(url_for('userlogin'))

app.run(debug=True)