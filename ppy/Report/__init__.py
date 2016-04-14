from flask import Blueprint

report = Blueprint('Report', __name__,
                        static_folder='static',
                        template_folder='templates')
print("11")
print(report.root_path)
print ("22")

import Views

