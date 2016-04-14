from flask import render_template, redirect, url_for, request, jsonify, flash


from ppy import services
from . import ad


# ad
@ad.route('/ad/ads')
def ads():
    return render_template("ad/adList.html", tag="ads")


@ad.route('/ad/ads/<adaction>')
def adsAction(adaction=None):
    return render_template("ad/adList.html", tag="ads", tagaction=adaction)


# banner
@ad.route('/banner/banners/<tag>')
def banners(tag=None):
    return render_template("ad/bannerList.html", tag=tag)


@ad.route('/banner/banners/<tag>/<tagaction>')
def bannerAction(tag=None, tagaction=None):
    return render_template("ad/bannerList.html", tag=tag, tagaction=tagaction)


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
