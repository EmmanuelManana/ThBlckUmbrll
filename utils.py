from models import Database


db = Database()

def register_user(username, firstname, lastname, email, password):
        sql_query = '''INSERT INTO USERS (Username, Firstname, Lastname, Email, Password) VALUES (?, ?, ?, ?, ?)'''
        user_info = (username, firstname, lastname, email, password)
        db.write_query(sql_query, user_info)