from flask import Blueprint

index = Blueprint('index', __name__,
                        static_folder='static',
                        template_folder='templates')
print("11")
print(index.root_path)
print ("22")

import Views