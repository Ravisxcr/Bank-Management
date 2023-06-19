import mysql
class Datbase:

    def __init__(self):
        self.__uname = 'master'
        self.__upass = 'nopassword'

    def ref(self,musername, mpassword):

        try:
            if musername == self.__uname and mpassword == self.__upass:
                # db = mysql.connector.connect(host='b9hhck7wnz51bsehyc7w-mysql.services.clever-cloud.com',
                # database='b9hhck7wnz51bsehyc7w',
                # user='ufn0kwnys97w7zmr',
                # port='3306',
                # password='72aR1zfrW8RlIxfahZTH',
                # )

                db = mysql.connector.connect(host='localhost', user='root', password='ubuntu')

                return db, 'sucess'
            else:
                return False, 'Authentican failed'
        except:
            return False, 'some error occured'

        