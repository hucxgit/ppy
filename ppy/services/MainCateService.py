from ..utils import JsonFormat
from ..models import Model

#MainCateService
class MainCateService:
    def __init__(self):
        pass
    def __del__(self):
        pass
    def serviceMainCate(self):
        maincates = []
        for num in range(0, 10):
            maincate = Model.MainCate(num,"maincatetitle","pic address","on")
            maincates.append(maincate)
        return JsonFormat.MyEncoder().encode({"code": 200, "data": maincates, "msg": "success"})
