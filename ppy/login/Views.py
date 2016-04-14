from flask import render_template, redirect, url_for, request, jsonify,flash

from ppy import services
from . import login

# reportlist
@login.route('/report/reports')
def reports():
    return render_template("report/reportList.html", tag="reports")

 # report
@login.route('/reportlist')
def reportlist():
    reportType = request.args.get("reportType", 0, type=int)
    return services.ReportService().serviceReportListsByType(reportType)
