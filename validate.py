import re
import utils as utils
class Validate:

    def username(self,username, erros):
        users = utils.get_all_users(self)
        usernames = []
        for _user in users:
            usernames.append(_user[1])
        print(usernames)
        if not re.match('^[A-Za-z][A-Za-z0-9]{2,49}$', username):
            erros.append('The username must be an alpha numeric value beginning with a letter, 3 - 50 characters long.')
        if username in usernames:
                erros.append("username has been taken, try a different one")
    
    def email(self, email, errors):
        users = utils.get_all_users(self)
        emails = []
        for _user in users:
            emails.append(_user[4])
        print(emails)
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,100}$', email):
            errors.append('invalid email format')
        if email in emails:
            errors.append("Email Already exist")
    
    def password(self, password, password_confirm, errors):
        if not re.match(r'^.*(?=.{8,10})(?=.*[a-zA-Z])(?=.*?[A-Z])(?=.*\d)[a-zA-Z0-9!@£$%^&*()_+={}?:~\[\]]+$', password):
            errors.append('Password must have an uppercase, lowercase and a digit, 5 - 25 characters long.')
        
        if password != password_confirm:
            errors.append('Entered password do not match, Re-enter your passwords')
    
    def firstname_lastname(self, firstname, lastname, errors):
        if not re.match('^[A-Z][a-zA-Z-]{1,24}$', firstname):
            errors.append('A name must start with a capital letter, and a have no more than 25 characters')
        if not re.match('^[A-Z][ a-zA-Z-]{1,24}$', lastname):
            errors.append('The lastname must start with a capital letter, and have 2-24 charaters')