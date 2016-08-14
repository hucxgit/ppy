from ..utils import JsonFormat
from ..utils import HttpUtil
from ..models import Model
from ..utils import JsonFormat
import urllib2
import urllib
import types
from ppy import getConfigByKey

#MessageService
class MessageService:
    def __init__(self):
        pass
    def __del__(self):
        pass
    def serviceSendMessages(self,messageTitle,messageContent,messageUrl,messageImageUrl):
        print(messageTitle);
        print(messageContent);
        print(messageUrl);
        print(messageImageUrl);

        posturl = getConfigByKey("URL") +":"+ getConfigByKey("PORT") + "/message/sends"
        print(posturl)
        data = {"messageType": 1, "sendId": -1, "messageTitle": messageTitle, "messageContent": messageContent,
                "messageImg": messageImageUrl, "messageUrl": messageUrl}
        result = HttpUtil.post(posturl, data)

        # print(type(result))
        # r = JsonFormat.MyDecoder().decode(result)
        # print(r)
        # print(type(r))
        return result
    def serviceStatictis(self,type):
        posturl = getConfigByKey("URL") + ":" + getConfigByKey("PORT") + "/statistic/" + type
        print(posturl)
        result = HttpUtil.postNoData(posturl)
        r = JsonFormat.MyDecoder().decode(result)

        code = r["respCode"]
        msg = r["respDesc"]
        statistics = []

        for obj in r["statistics"]:
            inviteModel = Model.InviteModel(obj["nickName"], obj["mobile"], obj["sums"])
            statistics.append(inviteModel)
        return JsonFormat.MyEncoder().encode({"code": code, "data": statistics, "msg": msg})






