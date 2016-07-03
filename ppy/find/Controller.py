# -*- coding: utf-8 -*-
from flask import  redirect, url_for, request
from ppy import services
from werkzeug import secure_filename
import tempfile
from . import find


#################
# find
# maincates
@find.route("/maincatelist")
def maincatelist():
    return services.MainCateService().serviceMainCate(0)


@find.route("/maincatesubmit", methods=['POST'])
def maincatesubmit():
    if request.method == 'POST':
        print("maincatesubmit")

        categoryId = request.form["cId"]
        categoryName = request.form['maincateName']
        f = request.files['inputfile']

        if categoryId == "":
            print ("create new banner")
            result = services.MainCateService().serviceNewCategory(categoryName,0)
            categoryId = result["categoryId"]
            filename = secure_filename(f.filename)
            if filename != "":
                path = tempfile.gettempdir() + filename
                spath = tempfile.gettempdir() + "s_" + filename
                f.save(path)
                f.save(spath)
                services.ImageUploadService().uploadCategoryImage("categoryId",categoryId, path, spath)
                print("上传图片结束")
        else:
            print ("update old banner")
            filename = secure_filename(f.filename)
            if filename != "":
                path = tempfile.gettempdir() + filename
                spath = tempfile.gettempdir() + "s_" + filename
                f.save(path)
                f.save(spath)
                services.ImageUploadService().uploadCategoryImage("categoryId",categoryId, path, spath)
                print("上传图片结束")
            print ("开始update其他数据")
            result = services.MainCateService().serviceUpdateMainCate(categoryId,categoryName)
        return redirect(url_for('find.maincate'))
    return ''


@find.route("/maincateedit/<categoryId>")
def maincateedit(categoryId=None):
    print ("enter controller ")
    print (categoryId)
    print ("enter controller ")
    data = services.MainCateService().serviceSelectMainCate(categoryId)
    return data


@find.route("/maincatedelete/<categoryId>")
def maincatedelete(categoryId=None):
    return services.MainCateService().serviceDeleteMainCate(categoryId)






# forumcate
@find.route("/forumcatelist")
def forumcatelist():
    parentid = request.args.get("parentid", 0, type=int)
    return services.ForumCateService().serviceForumCate(parentid)
    pass



@find.route("/forumcatesubmit", methods=['POST'])
def forumcatesubmit():
    if request.method == 'POST':
        print("forumcatesubmit")
        print(request)
        print (request.form)
        print (request.files)

        print("forumcatesubmit....")
        return redirect(url_for('forumcate'))
    return ''


@find.route("/forumcatedelete/<id>")
def forumcatedelete(id=None):
    return "forumcatedelete"






# anony
@find.route("/anonylist")
def anonylist():
    parentid = request.args.get("parentid", 0, type=int)
    return services.AnonyService().serviceAnony(parentid)


@find.route("/anonysubmit", methods=['POST'])
def anonysubmit():
    if request.method == 'POST':
        print("anonysubmit")
        print(request)
        print (request.form)
        print (request.files)

        print("anonysubmit....")
        return redirect(url_for('anony'))
    return ''


@find.route("/anonydelete/<id>")
def anonydelete(id=None):
    return "anonydelete"






# articlelist
@find.route("/articlelist")
def articlelist():
    articleType = request.args.get("articleType", 0, type=int)
    return services.ArticleService().serviceArticles(articleType)


@find.route("/articlesubmit", methods=['POST'])
def articlesubmit():
    if request.method == 'POST':
        print("articlesubmit")
        print(request)
        print (request.form)
        print (request.files)

        print("articlesubmit....")
        return redirect(url_for('article'))
    return ''


@find.route("/articledelete/<id>")
def articledelete(id=None):
    return "articledelete"