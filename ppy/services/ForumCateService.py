from ..utils import JsonFormat
from ..models import Model
from ppy import getConfigByKey
from ..utils import HttpUtil

#ForumCateServicd
class ForumCateService:
    def __init__(self):
        pass
    def __del__(self):
        pass
    def serviceForumCate(self,parentid,categoryType):
        print(parentid)
        posturl = getConfigByKey("URL") + ":" + getConfigByKey("PORT") + "/category/queryBatch"
        print(posturl)
        data = {"categoryTypeList": [categoryType],"parentId":parentid}
        result = HttpUtil.post(posturl, data)

        print("===============ForumCateService service list 1 ====================");
        print(result)
        print(type(result))
        r = JsonFormat.MyDecoder().decode(result)
        print(r)
        print(type(r))
        print("===============ForumCateService service list 2 ====================");
        code = r["respCode"]
        msg = r["respDesc"]
        categorys = []

        for obj in r["categorys"]:
            category = Model.MainCate(obj["categoryId"], obj["name"], obj["imageUrl"], obj["isDelete"], obj["parentId"],
                                      obj["created"])
            categorys.append(category)
        return JsonFormat.MyEncoder().encode({"code": code, "data": categorys, "msg": msg})

