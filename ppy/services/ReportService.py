from ..utils import JsonFormat
from ..models import Model
from ppy import getConfigByKey
from ..utils import HttpUtil

#ReportService
class ReportService():
    def __init__(self):
        pass
    def __del__(self):
        pass
    def serviceReportListsByType(self,reportType):
        print(reportType)

        posturl = getConfigByKey("URL") + ":" + getConfigByKey("PORT") + "/tsreport/queryreports"
        result = HttpUtil.postNoData(posturl)

        print("===============report service result 1 ====================");
        print(result)
        print(type(result))
        r = JsonFormat.MyDecoder().decode(result)
        print(r)
        print(type(r))
        print("===============report service result 2 ====================");


        code = r["respCode"]
        msg = r["respDesc"]
        reports = []

        for obj in r["tsReportContent"]:
            tsreport = obj["tsReport"]
            user = obj["user"]
            report = Model.Report(tsreport["id"],user["nickname"],tsreport["categoryType"],
                                  tsreport["reportType"],"reportcontent"
                                  ,tsreport["reason"],tsreport["created"])
            reports.append(report)
        return JsonFormat.MyEncoder().encode({"code": 200, "data": reports, "msg": "success"})

