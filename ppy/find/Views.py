from flask import render_template, redirect, url_for, request, jsonify, flash


from ppy import services
from . import find


@find.route('/find/maincate')
def maincate():
    return render_template("find/mainCateList.html", tag="maincate")


@find.route('/find/maincate/<maincateaction>')
def maincateAction(maincateaction=None):
    return render_template("find/mainCateList.html", tag="maincate", tagaction=maincateaction)


@find.route('/find/forumcate')
def forumcate():
    return render_template("find/forumcateList.html", tag="forumcate")


@find.route('/find/forumcate/<forumcateaction>')
def forumcateAction(forumcateaction=None):
    return render_template("find/forumcateList.html", tag="forumcate", tagaction=forumcateaction)


# annoy
@find.route('/find/anony')
def anony():
    return render_template("find/anonyList.html", tag="anony")


@find.route('/find/anony/<anonyaction>')
def anonyAction(anonyaction=None):
    return render_template("find/anonyList.html", tag="anony", tagaction=anonyaction)


# article
@find.route('/find/article')
def article():
    return render_template("find/articleList.html", tag="article")


@find.route('/find/article/<articleaction>')
def articleAction(articleaction=None):
    return render_template("find/articleList.html", tag="article", tagaction=articleaction)


#################
# find
# maincates
@find.route("/maincatelist")
def maincatelist():
    return services.MainCateService().serviceMainCate()


@find.route("/maincatesubmit", methods=['POST'])
def maincatesubmit():
    if request.method == 'POST':
        print("maincatesubmit")
        print(request)
        print (request.form)
        print (request.files)

        print("maincatesubmit....")
        return redirect(url_for('maincate'))
    return ''


@find.route("/maincatedelete/<id>")
def maincatedelete(id=None):
    return "maincatedelete"


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
