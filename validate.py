import re
import utils as utils
class Validate:

    def username(self,username, erros):
        users = utils.get_all_users(self)
        if not re.match('^[A-Za-z][A-Za-z0-9]{2,49}$', username):
            erros.append('The username must be an alpha numeric \
            value beginning with a letter, 3 - 50 characters long.')
        for user in users:
            if username == user[1]:
                erros.append("username has been taken, try a different one")