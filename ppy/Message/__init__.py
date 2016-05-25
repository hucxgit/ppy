from flask import Blueprint

Message = Blueprint('Message', __name__,
                        static_folder='static',
                        template_folder='templates')

import Views,Controller