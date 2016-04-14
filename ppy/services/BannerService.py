from ..utils import JsonFormat
from ..models import Model

#BannerService
class BannerService:
    def __init__(self):
        pass
    def __del__(self):
        pass
    def serviceMainBannerList(self):
        mainBannerList = []
        for num in range(0, 5):
            banner = Model.Banner("indexpage","http://www.baidu.com","1.jpg","running")
            mainBannerList.append(banner)
        return JsonFormat.MyEncoder().encode({"code": 200, "data": mainBannerList, "msg": "success"})

    def serviceForumBannerList(self):
        forumBannerList = []
        for num in range(0, 5):
            banner = Model.Banner("indexpage", "http://www.baidu.com", "1.jpg", "running")
            forumBannerList.append(banner)
        return JsonFormat.MyEncoder().encode({"code": 200, "data": forumBannerList, "msg": "success"})
