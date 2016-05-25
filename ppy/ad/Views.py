from flask import render_template, redirect, url_for
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



