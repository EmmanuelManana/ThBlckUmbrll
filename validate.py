import re
from models import Database


class Validate:

    def validate_username(self,username, erros):
        if not re.match('^[A-Za-z][A-Za-z0-9]{2,49}$', username):
            erros.append('The username must be an alpha numeric \
            value beginning with a letter, 3 - 50 characters long.')
    
