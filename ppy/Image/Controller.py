# -*- coding: utf-8 -*-
from flask import request,redirect,url_for
from werkzeug import secure_filename
import tempfile
from ppy import services
from . import Image

from ppy import services
@Image.route('/uploadImage',methods=['POST'])
def uploadImage():
    if request.method == 'POST':
        print ("forumbannersubmit")
        f = request.files['inputfile']
        filename = secure_filename(f.filename)
        if filename != "":
            path = tempfile.gettempdir() + filename
            spath = tempfile.gettempdir() + "s_" + filename
            f.save(path)
            f.save(spath)
            print (path)
            print (spath)
            return services.ImageUploadService().uploadPostImage("", "", path, spath)
        return ''
    return ''
