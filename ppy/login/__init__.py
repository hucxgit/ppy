from flask import Blueprint

login = Blueprint('login', __name__,
                        static_folder='static',
                        template_folder='templates')
print("11")
print(login.root_path)
print ("22")

import Views