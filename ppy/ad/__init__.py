from flask import Blueprint

ad = Blueprint('ad', __name__,
                        static_folder='static',
                        template_folder='templates')

import Views,Controller