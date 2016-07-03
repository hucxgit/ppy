from flask import Blueprint

report = Blueprint('Report', __name__,
                        static_folder='static',
                        template_folder='templates')

import Views,Controller

