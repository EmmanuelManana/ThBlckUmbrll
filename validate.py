import re
import utils as utils
class Validate:

    def username(self,username, erros):
        users = utils.get_all_users(self)
        usernames = []
        for _username in users:
            usernames.append(_username[1])
        print(usernames)
        if not re.match('^[A-Za-z][A-Za-z0-9]{2,49}$', username):
            erros.append('The username must be an alpha numeric \
            value beginning with a letter, 3 - 50 characters long.')
        if username in usernames:
                erros.append("username has been taken, try a different one")
    
    def email(self, email, erros):
        users = utils.get_all_users(self)
        emails = []
        for _email in users:
            emails.append(_email[4])
        print(emails)
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,100}$', email):
            errors.append('invalid email format')
        if email in emails:
            erros.append("Email Already exist")