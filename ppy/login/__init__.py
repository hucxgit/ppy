from flask import Blueprint

login = Blueprint('login', __name__,
                        static_folder='static',
                        template_folder='templates')

import Views,Controller