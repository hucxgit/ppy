from flask import render_template, redirect, url_for, request, jsonify,flash
from . import index

@index.route('/')
def main():
    return render_template("main.html")
