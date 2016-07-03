# -*- coding:utf-8 -*-
from ..utils import JsonFormat
from ..models import Model
from ppy import getConfigByKey
from ..utils import HttpUtil

#MainCateService
class MainCateService:
    def __init__(self):
        pass
    def __del__(self):
        pass
    def serviceMainCate(self,categoryType):
        posturl = getConfigByKey("URL") + ":" + getConfigByKey("PORT") + "/category/query"
        print(posturl)
        data = {"categoryType": categoryType}
        result = HttpUtil.post(posturl, data)

        print("===============MainCateService service list 1 ====================");
        print(result)
        print(type(result))
        r = JsonFormat.MyDecoder().decode(result)
        print(r)
        print(type(r))
        print("===============MainCateService service list 2 ====================");
        code = r["respCode"]
        msg = r["respDesc"]
        categorys = []

        for obj in r["categorys"]:
            category = Model.MainCate(obj["categoryId"], obj["name"], obj["imageUrl"], obj["isDelete"], obj["parentId"],
                                  obj["created"])
            categorys.append(category)
        return JsonFormat.MyEncoder().encode({"code": code, "data": categorys, "msg": msg})

    #根据id查询分类
    def serviceSelectMainCate(self,categoryId):
        posturl = getConfigByKey("URL") + ":" + getConfigByKey("PORT") + "/category/querybyid"
        print(posturl)
        data = {"categoryId": categoryId}
        result = HttpUtil.post(posturl, data)

        print("===============MainCateService service select by categoryid1 ====================");
        print(result)
        print(type(result))
        r = JsonFormat.MyDecoder().decode(result)
        print(r)
        print(type(r))
        print("===============MainCateService service select by categoryid2====================");

        code = r["respCode"]
        msg = r["respDesc"]
        print(r["categorys"])

        obj = r["categorys"];
        if len(obj) == 1:
            tmp = obj[0]
            category = Model.MainCate(tmp["categoryId"], tmp["name"], tmp["imageUrl"], tmp["isDelete"], tmp["parentId"],
                                      tmp["created"])
            result = JsonFormat.MyEncoder().encode({"code": 200, "msg": "msg", "data": category})
            return result
        else:
            return JsonFormat.MyEncoder().encode({"code": 200, "msg": "msg"})
        pass


    #根据id更新分类
    def serviceUpdateMainCate(self):
        pass

    def serviceUpdateMainCate(self, categoryId,categoryName):
        posturl = getConfigByKey("URL") + ":" + getConfigByKey("PORT") + "/category/update"
        print(posturl)
        data = {"categoryId": categoryId, "name": categoryName}
        result = HttpUtil.post(posturl, data)

        print("===============MainCateService service update result 1 ====================");
        print(result)
        print(type(result))
        r = JsonFormat.MyDecoder().decode(result)
        print(r)
        print(type(r))
        print("===============MainCateService service update result 2 ====================");

        code = r["respCode"]
        msg = r["respDesc"]
        return JsonFormat.MyEncoder().encode({"code": code, "msg": msg})

    #根据id删除分类
    def serviceDeleteMainCate(self,categoryId):
        posturl = getConfigByKey("URL") + ":" + getConfigByKey("PORT") + "/category/delete"
        print(posturl)
        data = {"categoryId": categoryId}
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


    ##新建分类
    def serviceNewCategory(self, name, categoryType):
        print ("=================================================")
        posturl = getConfigByKey("URL") + ":" + getConfigByKey("PORT") + "/category/create"
        print(posturl)
        data = { "name": name, "categoryType": categoryType, "imageUrl": "--"}
        result = HttpUtil.post(posturl, data)

        print("===============MainCateService service create result 1 ====================");
        print(result)
        print(type(result))
        r = JsonFormat.MyDecoder().decode(result)
        print(r)
        print(type(r))
        print("===============MainCateService service create result 2 ====================");
        return r
        pass