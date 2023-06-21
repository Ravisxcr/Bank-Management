from sqlalchemy import create_engine, text

engine = create_engine("mysql://root:ubuntu@localhost/bank",echo = True)

def check_ulogin(uname, upass):
    with engine.connect() as conn:
        result = conn.execute(text("select * from account_login where Account_number = :acc"),acc=uname)
        result = result.all()
        if len(result) > 0 and upass == result[0][1]:
            return True
        else:
            return False
    
def acc_details(acc_no):
    with engine.connect() as conn:
        result = conn.execute(text("select * from accounts where Account_number = :acc"),acc=acc_no)
        return result.all()
    
def branch_details(branch_code):
    with engine.connect() as conn:
        result = conn.execute(text("select * from branch where Branch_code = :branch_code"),branch_code=branch_code)
        return result.all()
    
def acc_tranaction(acc_no):
    with engine.connect() as conn:
        result = conn.execute(text("select * from tranaction where Account_number = :acc order by tr_time desc"),acc=acc_no)
        return result.all()
    
def ubalance(acc_no):
    with engine.connect() as conn:
        result = conn.execute(text("select Balance from accounts where Account_number = :acc"),acc=acc_no)
        return result.all()
    
def user_pay(data):
    print(data)
    if check_ulogin(data['uname'],data['upass']): 
        current_bal = ubalance(data['uname'])[0][0]
        if  current_bal> int(data["amount"]) + 50:
            with engine.connect() as conn:
                new_bal = current_bal-int(data['amount'])
                result = conn.execute(text("insert into tranaction (Tr_amount,  Tr_type,  Account_number,  tr_info, tr_balance) values (:amt, 'D', :acc, :trinfo, :trbal)"),amt=data['amount'],acc=data['uname'], trinfo='ONLINE_PAID_TO_'+str(data['payee']), trbal=new_bal)

                result = conn.execute(text('update accounts set Balance = :bal where  Account_number = :acc_no'),bal=new_bal, acc_no=data['uname'])
            return 'S'
        else:
            return 'IB'
    else:
        return 'F'


def check_elogin(uname, upass):
    with engine.connect() as conn:
        result = conn.execute(text("select * from employee where Emp_number = :emp_no"),emp_no=uname)
        result = result.all()
        if len(result) > 0 and str(upass) == result[0][6]:
            return True
        else:
            return False


def acc_emp(emp_no):
    emp_det , br_detail = None, None
    with engine.connect() as conn:
        emp_det = conn.execute(text("select Emp_number, Emp_name, Gender, Address, Designation, Branch_code from employee where Emp_number = :emp_no"),emp_no=emp_no)
        emp_det = emp_det.all()
        if len(emp_det) > 0:
            br_detail = branch_details(emp_det[0][5])
        
    return emp_det, br_detail
        

def all_tr():
    with engine.connect() as conn:
        tr = conn.execute(text("select * from tranaction order by tr_time desc"))
        return tr.all()

def all_customer():
    with engine.connect() as conn:
        query = conn.execute(text('select * from accounts'))
        return query.all()

def br_customer(br_code):
    with engine.connect() as conn:
        query = conn.execute(text('select * from accounts where Branch_code = :br_code'),br_code=br_code)
        return query.all()


