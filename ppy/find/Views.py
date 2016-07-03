from flask import render_template
from . import find


@find.route('/find/maincate_page')
def maincate():
    return render_template("find/mainCateList.html", tag="maincate")


@find.route('/find/maincate_page/<maincateaction>')
def maincateNew(maincateaction=None):
    return render_template("find/mainCateList.html", tag="maincate", tagaction=maincateaction)

@find.route('/find/maincate_page/<maincateaction>/<categoryId>')
def maincateAction(maincateaction=None,categoryId=None):
    return render_template("find/mainCateList.html", tag="maincate", tagaction=maincateaction,categoryId=categoryId)


@find.route('/find/forumcate_page')
def forumcate():
    return render_template("find/forumcateList.html", tag="forumcate")


@find.route('/find/forumcate_page/<forumcateaction>')
def forumcateAction(forumcateaction=None):
    return render_template("find/forumcateList.html", tag="forumcate", tagaction=forumcateaction)











# annoy
@find.route('/find/anony_page')
def anony():
    return render_template("find/anonyList.html", tag="anony")


@find.route('/find/anony_page/<anonyaction>')
def anonyAction(anonyaction=None):
    return render_template("find/anonyList.html", tag="anony", tagaction=anonyaction)


# article
@find.route('/find/article_page')
def article():
    return render_template("find/articleList.html", tag="article")


@find.route('/find/article_page/<articleaction>')
def articleAction(articleaction=None):
    return render_template("find/articleList.html", tag="article", tagaction=articleaction)



