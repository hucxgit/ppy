from flask import Blueprint

ad = Blueprint('ad', __name__,
                        static_folder='static',
                        template_folder='templates')
print("11")
print(ad.root_path)
print ("22")
import Views