from models import Database

db = Database()

def register_user(username, firstname, lastname, email, password):
        sql_query = '''INSERT INTO USERS (Username, Firstname, Lastname, Email, Password) VALUES (?, ?, ?, ?, ?)'''
        user_info = (username, firstname, lastname, email, password)
        db.write_query(sql_query, user_info)


def get_all_users():
        sql_query = 'SELECT * FROM Users'
        users = db.fetch_query(sql_query)
        return users #users of type list

def get_user(email):
        sql_query = 'SELECT * FROM Users WHERE  Email = ?'
        user = db.fetch_query(sql_query, email)
        return user #user is of type list