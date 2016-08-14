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
@find.route("/forumcatelist/<parentid>")
def forumcatelist(parentid=None):
    return services.ForumCateService().serviceForumCate(parentid,1)
    pass



@find.route("/forumcatesubmit", methods=['POST'])
def forumcatesubmit():
    if request.method == 'POST':
        print("forumcatesubmit")

        categoryId = request.form["cId"]
        categoryName = request.form['maincateName']
        f = request.files['inputfile']

        if categoryId == "":
            print ("create new banner")
            result = services.MainCateService().serviceNewCategory(categoryName, 1)
            categoryId = result["categoryId"]
            filename = secure_filename(f.filename)
            if filename != "":
                path = tempfile.gettempdir() + filename
                spath = tempfile.gettempdir() + "s_" + filename
                f.save(path)
                f.save(spath)
                services.ImageUploadService().uploadCategoryImage("categoryId", categoryId, path, spath)
                print("上传图片结束")
        else:
            print ("update old banner")
            filename = secure_filename(f.filename)
            if filename != "":
                path = tempfile.gettempdir() + filename
                spath = tempfile.gettempdir() + "s_" + filename
                f.save(path)
                f.save(spath)
                services.ImageUploadService().uploadCategoryImage("categoryId", categoryId, path, spath)
                print("上传图片结束")
            print ("开始update其他数据")
            result = services.MainCateService().serviceUpdateMainCate(categoryId, categoryName)
        return redirect(url_for('find.forumcate'))
    return ''


@find.route("/forumcateedit/<categoryId>")
def forumcateedit(categoryId=None):
    print ("enter controller ")
    print (categoryId)
    print ("enter controller ")
    data = services.MainCateService().serviceSelectMainCate(categoryId)
    return data


@find.route("/forumcatedelete/<categoryId>")
def forumcatedelete(categoryId=None):
    return services.MainCateService().serviceDeleteMainCate(categoryId)












# anony
@find.route("/anonylist/<parentid>")
def anonylist(parentid=None):
    return services.ForumCateService().serviceForumCate(parentid, 2)
    pass


@find.route("/anonysubmit", methods=['POST'])
def anonysubmit():
    if request.method == 'POST':
        print("forumcatesubmit")

        categoryId = request.form["cId"]
        categoryName = request.form['maincateName']
        f = request.files['inputfile']

        if categoryId == "":
            print ("create new banner")
            result = services.MainCateService().serviceNewCategory(categoryName, 2)
            categoryId = result["categoryId"]
            filename = secure_filename(f.filename)
            if filename != "":
                path = tempfile.gettempdir() + filename
                spath = tempfile.gettempdir() + "s_" + filename
                f.save(path)
                f.save(spath)
                services.ImageUploadService().uploadCategoryImage("categoryId", categoryId, path, spath)
                print("上传图片结束")
        else:
            print ("update old banner")
            filename = secure_filename(f.filename)
            if filename != "":
                path = tempfile.gettempdir() + filename
                spath = tempfile.gettempdir() + "s_" + filename
                f.save(path)
                f.save(spath)
                services.ImageUploadService().uploadCategoryImage("categoryId", categoryId, path, spath)
                print("上传图片结束")
            print ("开始update其他数据")
            result = services.MainCateService().serviceUpdateMainCate(categoryId, categoryName)
        return redirect(url_for('find.anony'))
    return ''

@find.route("/annoyedit/<categoryId>")
def annoyedit(categoryId=None):
    print ("enter controller ")
    print (categoryId)
    print ("enter controller ")
    data = services.MainCateService().serviceSelectMainCate(categoryId)
    return data


@find.route("/anonydelete/<categoryId>")
def anonydelete(categoryId=None):
    return services.MainCateService().serviceDeleteMainCate(categoryId)




# articlelist
@find.route("/articlelist/<articleType>")
def articlelist(articleType=None):
    print (articleType)
    print (type(articleType))
    categoryId = 0;
    if articleType == "0" :
        print ("微科普")
        categoryId = 16;#微科普
    else :
        print ("暖故事")
        categoryId = 14; #暖故事
    return services.ArticleService().serviceArticles(categoryId)


@find.route("/articlesubmit", methods=['POST'])
def articlesubmit():
    if request.method == 'POST':
        postId = request.form["pId"]
        author = request.form['articleAuthor']
        title = request.form['articleName']
        simpleContent = request.form['articleDes']
        content = request.form['editorarticle']
        categoryState = request.form['CategoryState']
        categoryId = 0;
        if categoryState == "0":
            print ("微科普")
            categoryId = 16;  # 微科普
        else:
            print ("暖故事")
            categoryId = 14;  # 暖故事

        if postId == "":
            result = services.ArticleService().serviceCreatePost("1",categoryId,author,title,simpleContent,content)
            print("新建帖子结果");
            print(result);
            return redirect(url_for('find.article'))
        else:
            result = services.ArticleService().serviceUpdatePost(postId,categoryId,author, title, simpleContent, content)
            return redirect(url_for('find.article'))
    return ''

@find.route("/articleedit/<postid>")
def articleedit(postid=None):
    print ("enter controller ")
    print (postid)
    print ("enter controller ")
    data = services.ArticleService().serviceArticleDetail(postid)
    return data


@find.route("/articledelete/<postid>")
def articledelete(postid=None):
    return services.ArticleService().serviceDeletePostById(postid)