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
      session['ecode'] = emp_code(session['user'])
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


# User withdrawl
@app.route('/transaction',methods=['POST','GET'])
def utranaction():
  return render_template('withdrawl.html')

# Employee deposit to User
@app.route('/deposit',methods=['POST','GET'])
def deposit():
  return render_template('deposit.html')

# Message when amount is debited
@app.route('/debit_msg', methods=['GET','POST'])
def debit_msg():
  if request.method == 'POST':
    data = request.form
    session['msg'] = user_pay(data)
    session['amt'] = data['amount']
    session['acc'] = data['uname']
    return redirect(url_for('debit_msgr'))
  return render_template('userlogin.html')

@app.route('/debit_msgr')
def debit_msgr():
  msg,amt,acc = None,None,None
  if 'msg' in session:
    msg = session['msg']
    session.pop('msg',None)
  if 'amt' in session:
    amt = session['amt']
    session.pop('amt',None)
  if 'acc' in session:
    acc = session['acc']
    session.pop('acc',None)
  return render_template('debit_msg.html', msg=msg, amt=amt, acc=acc)

# Message when amount is credited
@app.route('/credit_msg', methods=['POST','GET'])
def credit_msg():
  if request.method == 'POST' and g.user is not None:
    data = request.form
    session['msg'] = cr_amt(data,session['user'])
    session['amt'] = data['amount']
    session['payee'] = data['payee']
    return redirect(url_for('credit_msgr'))
  else:
    return render_template('userlogin.html')
  
@app.route('/credit_msgr', methods=['POST','GET'])
def credit_msgr():
  msg,amt,payee = None,None,None
  if 'msg' in session:
    msg = session['msg']
    session.pop('msg',None)
  if 'amt' in session:
    amt = session['amt']
    session.pop('amt',None)
  if 'payee' in session:
    payee = session['payee']
    session.pop('payee',None)
  return render_template('credit_msg.html', msg=msg, amt=amt, acc=payee)

# Account Opening
@app.route('/accopen', methods=['POST','GET'])
def accopen():
  if request.method == 'POST' and g.user is not None:
    data = request.form
    session['acc'],session['msg'] = new_acc(data)
    return redirect(url_for('accopen_msgr'))
  else:
    return render_template('userlogin.html')
  
@app.route('/accopen_msgr', methods=['POST','GET'])
def accopen_msgr():
  acc, msg = session['acc'],session['msg']
  if 'msg' in session:
    msg = session['msg']
    session.pop('msg',None)
  if 'acc' in session:
    acc = session['acc']
    session.pop('acc',None)
  return render_template('accopen_msg.html', msg=msg, acc=acc)


@app.route('/data', methods=['GET','POST'])
def data():
  return jsonify(request.form)



# Run before each request
@app.before_request
def before_request():
  g.user = None
  if 'user' in session:
    g.user = session['user']

# Logout
@app.route('/dropsession')
def dropsession():
  session.pop('user',None )
  if 'ecode' in session:
    session.pop('ecode',None)
  return redirect(url_for('userlogin'))

app.run(debug=True)