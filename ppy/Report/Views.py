from flask import render_template, redirect, url_for



from . import report

# reportlist
@report.route('/report/reports')
def reports():
    return render_template("report/reportList.html", tag="reports")

