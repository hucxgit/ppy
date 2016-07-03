from flask import Blueprint

index = Blueprint('index', __name__,
                        static_folder='static',
                        template_folder='templates')


import Views,Controller