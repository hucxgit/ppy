from flask import render_template, redirect, url_for
from . import Image
@Image.route('/image/uploadImage')
def uploadImagePage():
    return render_template("image/ImageContent.html", tag="image", tagaction="uploadImage")
    pass
