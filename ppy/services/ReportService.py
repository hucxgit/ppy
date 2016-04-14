from ..utils import JsonFormat
from ..models import Model

#ReportService
class ReportService():
    def __init__(self):
        pass
    def __del__(self):
        pass
    def serviceReportListsByType(self,reportType):
        print(reportType)
        reportlists = []
        for num in range(0, 3 * reportType + 1):
            report = Model.Report(num, "zs", 1, 1, "content not right", "invalid", "12:18")
            reportlists.append(report)
        return JsonFormat.MyEncoder().encode({"code": 200, "data": reportlists, "msg": "success"})
