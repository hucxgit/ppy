from ..utils import JsonFormat
from ..models import Model
from ppy import getConfigByKey
from ..utils import HttpUtil

class ImageUploadService:
    def __init__(self):
        pass
    def __del__(self):
        pass

    def uploadBannerImage(self,key,bannerId,path,spath):
        posturl = getConfigByKey("URL") + ":" + getConfigByKey("PORT") + "/images/uploadBanner"
        print(posturl)
        result = HttpUtil.uploadFile(posturl,path,spath,key,bannerId)

        print("===============mainBannerList uploadBannerImage result 1 ====================");
        print(result)
        print(type(result))
        r = JsonFormat.MyDecoder().decode(result)
        print(r)
        print(type(r))
        print("===============mainBannerList uploadBannerImage result 2 ====================");

        code = r["respCode"]
        msg = r["respDesc"]
        pass

    def uploadCategoryImage(self,key,categoryId,path,spath):
        posturl = getConfigByKey("URL") + ":" + getConfigByKey("PORT") + "/images/uploadCategory"
        print(posturl)
        result = HttpUtil.uploadFile(posturl, path, spath,key, categoryId)

        print("===============mainBannerList uploadBannerImage result 1 ====================");
        print(result)
        print(type(result))
        r = JsonFormat.MyDecoder().decode(result)
        print(r)
        print(type(r))
        print("===============mainBannerList uploadBannerImage result 2 ====================");

        code = r["respCode"]
        msg = r["respDesc"]
        pass
