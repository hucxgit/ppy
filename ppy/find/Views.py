from flask import render_template
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



