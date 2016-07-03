from flask import render_template
from . import index

@index.route('/index_page')
def index():
    return render_template("main.html")
