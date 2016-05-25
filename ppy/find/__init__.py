from flask import Blueprint

find = Blueprint('find', __name__,
                        static_folder='static',
                        template_folder='templates')

import Views,Controller
