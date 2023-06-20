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
    

