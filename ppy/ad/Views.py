from flask import render_template, redirect, url_for
from . import ad


# ad
@ad.route('/ad/ads_page')
def ads():
    return render_template("ad/adList.html", tag="ads")


@ad.route('/ad/ads_page/<adaction>')
def adsAction(adaction=None):
    return render_template("ad/adList.html", tag="ads", tagaction=adaction)


# banner
@ad.route('/banner/banners_page/<tag>')
def banners(tag=None):
    return render_template("ad/bannerList.html", tag=tag)

@ad.route('/banner/banners_page/<tag>/<tagaction>')
def bannerNew(tag=None, tagaction=None,bannerId=None):
    return render_template("ad/bannerList.html", tag=tag, tagaction=tagaction)

@ad.route('/banner/banners_page/<tag>/<tagaction>/<bannerId>')
def bannerAction(tag=None, tagaction=None,bannerId=None):
    return render_template("ad/bannerList.html", tag=tag, tagaction=tagaction,bannerId=bannerId)

