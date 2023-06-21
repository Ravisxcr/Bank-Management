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
        if  current_bal> int(data["amount"]) :
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

def emp_exits(emp_no):
    with engine.connect() as conn:
        result = conn.execute(text("select * from employee where Emp_number = :emp_no"),emp_no=emp_no)
        result = result.all()
        if len(result) > 0:
            return True
        else:
            return False

def cus_exist(acc_no):
    with engine.connect() as conn:
        result = conn.execute(text("select * from account_login where Account_number = :acc"),acc=acc_no)
        result = result.all()
        print(result)
        if len(result) > 0 :
            return True
        else:
            return False
        
def emp_code(emp_no):
    with engine.connect() as conn:
        query = conn.execute(text('select Branch_code from employee where Emp_number = :emp_no'),emp_no=emp_no)
        return query.all()[0][0]

def cr_amt(data,emp):
    if emp_exits(emp) and check_elogin(emp,data['epass']):
        if cus_exist(data['payee']):
            current_bal = ubalance(data['payee'])[0][0]
            with engine.connect() as conn:
                new_bal = current_bal+int(data['amount'])
                result = conn.execute(text("insert into tranaction (Tr_amount,  Tr_type,  Account_number,  tr_info, tr_balance) values (:amt, 'C', :acc, :trinfo, :trbal)"),amt=data['amount'],acc=data['payee'], trinfo='Cash Deposit '+str(data['payee']), trbal=new_bal)
                result = conn.execute(text('update accounts set Balance = :bal where  Account_number = :acc_no'),bal=new_bal, acc_no=data['payee'])
            return 'S'
        else:
            return 'NO'
    else:
        return 'F'


def branch_code(branch):
    with engine.connect() as conn:
        query = conn.execute(text('select Branch_code from branch where Branch_name = :branch'),branch=branch)
        return query.all()[0][0]  

def new_acc(data):
    with engine.connect() as conn:
        acc_type = data['acc_type']
        amt = data['amt']
        branch = data['branch']
        gender = data['gender']
        uadd = data['uadd']
        name = data['uname']
        upass  = data['upass']
        br_code = branch_code(branch)
        try:
            query = conn.execute(text('select Account_number from accounts where Account_name = :name and Gender = :gender and Address = :uadd and Balance = :amt and Account_type = :acc_type and Branch_code = :br_code'),name=name, gender=gender, uadd=uadd, amt=amt, acc_type=acc_type, br_code=br_code)
            acc_no = query.all()[0][0]
            return acc_no, 'A'
        except IndexError:
            query = conn.execute(text('insert into accounts (Account_name, Gender, Address, Balance , Account_type, Branch_code) values (:name, :gender, :uadd, :amt, :acc_type, :br_code)'),name=name, gender=gender, uadd=uadd, amt=amt, acc_type=acc_type, br_code=br_code)
            query = conn.execute(text('select Account_number from accounts where Account_name = :name and Gender = :gender and Address = :uadd and Balance = :amt and Account_type = :acc_type and Branch_code = :br_code'),name=name, gender=gender, uadd=uadd, amt=amt, acc_type=acc_type, br_code=br_code)
            acc_no = query.all()[0][0]
            print('Accountftgyhuj   ',acc_no)
            result = conn.execute(text('insert into account_login (Account_number, Password) values (:acc_no, :upass)'),acc_no=acc_no, upass=upass)
            return acc_no, 'N'