from flask import request,redirect,url_for
from ppy import services
from . import ad


# adlist
@ad.route("/adlist")
def adlist():
    adPlace = request.args.get("adPlace", 0, type=int)
    return services.AdService().serviceAdsByplace(adPlace)


# may be add or update
@ad.route("/adsubmit", methods=['POST'])
def adsubmit():
    if request.method == 'POST':
        print("newAdd")
        print(request)
        print (request.form)
        print (request.files)

        print("newAdd....")
        # session['username'] = request.form['username']
        # print(request.form['adTitle'])
        return redirect(url_for('ads'))
    return ''


@ad.route("/addelete/<id>")
def addelete(id=None):
    return "addelete"


# banner
@ad.route("/mainbannerlist")
def mainbannerlist():
    return services.BannerService().serviceMainBannerList()


@ad.route("/mainbannersubmit", methods=['POST'])
def mainbannersubmit():
    if request.method == 'POST':
        print("mainbannerSubmit")
        print(request)
        print (request.form)
        print (request.files)

        print("mainbannerSubmit....")
        return redirect(url_for('banners', tag="mainbanner"))
    return ''


@ad.route("/mainbannerdelete/<id>")
def mainbannerdelete(id=None):
    return "mainbannerdelete"


@ad.route("/forumbannerlist")
def forumbannerlist():
    return services.BannerService().serviceForumBannerList()


@ad.route("/forumbannersubmit", methods=['POST'])
def forumbannersubmit():
    if request.method == 'POST':
        print("forumbannersubmit")
        print(request)
        print (request.form)
        print (request.files)

        print("forumbannersubmit....")
        return redirect(url_for('banners', tag="forumbanner"))
    return ''


@ad.route("/forumbannerdelete/<id>")
def forumbannerdelete(id=None):
    return "forumbannerdelete"