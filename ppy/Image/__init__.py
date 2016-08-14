from flask import Blueprint

Image = Blueprint('Image', __name__,
                        static_folder='static',
                        template_folder='templates')

import Views,Controller