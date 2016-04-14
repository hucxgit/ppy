from ..utils import JsonFormat
from ..models import Model

#AnonyService
class AnonyService:
    def __init__(self):
        pass
    def __del__(self):
        pass

    def serviceAnony(self, parentid):
        print(parentid)
        anonys = []
        for num in range(0, parentid * 5 + 5):
            anony = Model.AnonyCate(num, "anonyName", "anonyPic", "anonyState")
            anonys.append(anony)
        return JsonFormat.MyEncoder().encode({"code": 200, "data": anonys, "msg": "success"})
