from ..utils import JsonFormat
from ..models import Model

#AdService
class AdService:
    def __init__(self):
        pass
    def __del__(self):
        pass
    def serviceAdsByplace(self,adPlace):
        print(adPlace)
        ads = []
        for num in range(0, 3 * adPlace + 1):
            ad = Model.Adviertisement( "title","http://cda.net.cn/cda/","global"," 2015-11-06 12:41 2016-01-01 00:00","on")
            ads.append(ad)
        return JsonFormat.MyEncoder().encode({"code": 200, "data": ads, "msg": "success"})
