from ..utils import JsonFormat
from ..models import Model

#ForumCateServicd
class ForumCateService:
    def __init__(self):
        pass
    def __del__(self):
        pass
    def serviceForumCate(self,parentid):
        print(parentid)
        forumncates = []
        for num in range(0, parentid*5 + 5):
            forumcate = Model.ForumCate(num,"forumcateName","forumcatePic","forumcateState")
            forumncates.append(forumcate)
        return JsonFormat.MyEncoder().encode({"code": 200, "data": forumncates, "msg": "success"})
