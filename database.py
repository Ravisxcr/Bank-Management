from sqlalchemy import create_engine, text

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


        