# -*- coding: utf-8 -*-
from flask import request,redirect,url_for
from werkzeug import secure_filename
import tempfile
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
        return redirect(url_for('ad.ads'))
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
        print ("forumbannersubmit")
        bannerId = request.form["bId"]
        bannerUrl = request.form['bannerUrl']
        bannerName = request.form['bannerName']
        f = request.files['inputfile']

        if bannerId == "":
            print ("create new banner")
            result = services.BannerService().serviceNewBanner(0, bannerName, bannerUrl, 0)
            bannerId = result["id"]
            filename = secure_filename(f.filename)
            if filename != "":
                path = tempfile.gettempdir() + filename
                spath = tempfile.gettempdir() + "s_" + filename
                f.save(path)
                f.save(spath)
                services.ImageUploadService().uploadBannerImage("bannerId",bannerId, path, spath)
                print("上传图片结束")
        else:
            print ("update old banner")
            filename = secure_filename(f.filename)
            if filename != "":
                path = tempfile.gettempdir() + filename
                spath = tempfile.gettempdir() + "s_" + filename
                f.save(path)
                f.save(spath)
                services.ImageUploadService().uploadBannerImage("bannerId",bannerId, path, spath)
                print("上传图片结束")
            print ("开始update其他数据")
            result = services.BannerService().serviceUpdateBanner(bannerId, 0, bannerName, bannerUrl)
        return redirect(url_for('ad.banners', tag="mainbanner"))
    return ''

@ad.route("/mainbanneredit/<bannerId>")
def mainbanneredit(bannerId=None):
    data = services.BannerService().serviceMainBannerEditById(bannerId)
    return data


@ad.route("/mainbannerdelete/<bannerId>")
def mainbannerdelete(bannerId=None):
    return services.BannerService().serviceMainBannerDeleteById(bannerId)






@ad.route("/forumbannerlist")
def forumbannerlist():
    return services.BannerService().serviceForumBannerList()


@ad.route("/forumbannersubmit", methods=['POST'])
def forumbannersubmit():
    if request.method == 'POST':
        print ("forumbannersubmit")
        bannerId = request.form["bId"]
        bannerUrl = request.form['bannerUrl']
        bannerName = request.form['bannerName']
        f = request.files['inputfile']

        if bannerId == "":
            print ("create new banner")
            result = services.BannerService().serviceNewBanner(1,bannerName,bannerUrl,0)
            bannerId = result["id"]
            filename = secure_filename(f.filename)
            if filename != "":
                path = tempfile.gettempdir() + filename
                spath = tempfile.gettempdir() + "s_" + filename
                f.save(path)
                f.save(spath)
                services.ImageUploadService().uploadBannerImage("bannerId",bannerId, path, spath)
                print("上传图片结束")
        else:
            print ("update old banner")
            filename = secure_filename(f.filename)
            if filename != "":
                path = tempfile.gettempdir() + filename
                spath = tempfile.gettempdir() + "s_" + filename
                f.save(path)
                f.save(spath)
                services.ImageUploadService().uploadBannerImage("bannerId",bannerId, path, spath)
                print("上传图片结束")
            print ("开始update其他数据")
            result = services.BannerService().serviceUpdateBanner(bannerId, 1, bannerName, bannerUrl)


        return redirect(url_for('ad.banners', tag="forumbanner"))
    return ''

@ad.route("/forumbanneredit/<bannerId>")
def forumbanneredit(bannerId=None):
    data = services.BannerService().serviceMainBannerEditById(bannerId)
    return data


@ad.route("/forumbannerdelete/<bannerId>")
def forumbannerdelete(bannerId=None):
    return services.BannerService().serviceForumBannerDeleteById(bannerId)