from flask import Blueprint

find = Blueprint('find', __name__,
                        static_folder='static',
                        template_folder='templates')
print("11")
print(find.root_path)
print ("22")
import Views
