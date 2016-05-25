from flask import request

from . import report
from ppy import services


# report
@report.route('/reportlist')
def reportlist():
    reportType = request.args.get("reportType", 0, type=int)
    return services.ReportService().serviceReportListsByType(reportType)
