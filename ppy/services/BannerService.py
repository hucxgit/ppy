# -*- coding:utf-8 -*-
from ..utils import JsonFormat
from ..models import Model
from ppy import getConfigByKey
from ..utils import HttpUtil


#BannerService
class BannerService:
    def __init__(self):
        pass
    def __del__(self):
        pass

    ##查询列表
    def serviceMainBannerList(self):
        return self.serviceBannerByModule(0)

    def serviceForumBannerList(self):
        return self.serviceBannerByModule(1)

    ##查询一个banner
    def serviceMainBannerEditById(self,bannerId):
        return self.serviceEditBannerById(bannerId)

    def serviceForumBannerEditById(self,bannerId):
        return self.serviceEditBannerById(bannerId)

    ##删除banner
    def serviceMainBannerDeleteById(self,bannerId):
        return self.serviceDeleteBannerById(bannerId)
        pass
    def serviceForumBannerDeleteById(self, bannerId):
        return self.serviceDeleteBannerById(bannerId)
        pass



    #根据module查询banner
    def serviceBannerByModule(self,modules):
        posturl = getConfigByKey("URL") + ":" + getConfigByKey("PORT") + "/banner/query"
        print(posturl)
        data = {"modules": modules}
        result = HttpUtil.post(posturl, data)

        print("===============mainBannerList service result 1 ====================");
        print(result)
        print(type(result))
        r = JsonFormat.MyDecoder().decode(result)
        print(r)
        print(type(r))
        print("===============mainBannerList service result 2 ====================");


        code = r["respCode"]
        msg = r["respDesc"]
        mainBannerList = []

        for obj in r["banners"]:
            banner = Model.Banner(obj["bannerId"], obj["name"], obj["bannerUrl"], obj["imageUrl"], obj["isDelete"],
                                  obj["created"])
            mainBannerList.append(banner)
        return JsonFormat.MyEncoder().encode({"code": code, "data": mainBannerList, "msg": msg})

    def serviceDeleteBannerById(self,bannerId):
         posturl = getConfigByKey("URL") + ":" + getConfigByKey("PORT") + "/banner/delete"
         print(posturl)
         data = {"bannerId": bannerId}
         result = HttpUtil.post(posturl, data)

         print("===============mainBannerList service delete result 1 ====================");
         print(result)
         print(type(result))
         r = JsonFormat.MyDecoder().decode(result)
         print(r)
         print(type(r))
         print("===============mainBannerList service delete result 2 ====================");
         code = r["respCode"]
         msg = r["respDesc"]
         return JsonFormat.MyEncoder().encode({"code": code, "msg": msg})

    def serviceEditBannerById(self,bannerId):
        posturl = getConfigByKey("URL") + ":" + getConfigByKey("PORT") + "/banner/querybyid"
        print(posturl)
        data = {"bannerId": bannerId}
        result = HttpUtil.post(posturl, data)

        print("===============mainBannerList service select result 1 ====================");
        print(result)
        print(type(result))
        r = JsonFormat.MyDecoder().decode(result)
        print(r)
        print(type(r))
        print("===============mainBannerList service select result 2 ====================");

        code = r["respCode"]
        msg = r["respDesc"]
        print(r["banners"])

        obj = r["banners"];
        if len(obj) == 1 :
             tmp = obj[0]
             banner = Model.Banner(tmp["bannerId"], tmp["name"], tmp["bannerUrl"], tmp["imageUrl"], tmp["isDelete"],
                                   tmp["created"])
             result = JsonFormat.MyEncoder().encode({"code": 200, "msg":"msg","data":banner})
             return result
        else:
             return JsonFormat.MyEncoder().encode({"code": 200, "msg": "msg"})


     ##更新banner
    def serviceUpdateBanner(self, bannerId, modules,bannerName, bannerUrl):
        posturl = getConfigByKey("URL") + ":" + getConfigByKey("PORT") + "/banner/update"
        print(posturl)
        data = {"bannerId": bannerId,"modules":modules,"name":bannerName,"bannerUrl":bannerUrl}
        result = HttpUtil.post(posturl, data)

        print("===============mainBannerList service update result 1 ====================");
        print(result)
        print(type(result))
        r = JsonFormat.MyDecoder().decode(result)
        print(r)
        print(type(r))
        print("===============mainBannerList service update result 2 ====================");

        code = r["respCode"]
        msg = r["respDesc"]
        return JsonFormat.MyEncoder().encode({"code": code, "msg": msg})

    ##新建banner
    def serviceNewBanner(self,modules,bannerName,bannerUrl,weight):
        print ("=================================================")
        posturl = getConfigByKey("URL") + ":" + getConfigByKey("PORT") + "/banner/create"
        print(posturl)
        data = { "modules": modules, "name": bannerName, "bannerUrl": bannerUrl,"imageUrl":"--","weight":weight}
        result = HttpUtil.post(posturl, data)

        print("===============mainBannerList service create result 1 ====================");
        print(result)
        print(type(result))
        r = JsonFormat.MyDecoder().decode(result)
        print(r)
        print(type(r))
        print("===============mainBannerList service create result 2 ====================");
        return r
        pass


