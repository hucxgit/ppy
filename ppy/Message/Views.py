from flask import render_template, redirect, url_for
from . import Message
@Message.route('/message/messages/sends_page')
def sendsMessage():
    return render_template("message/messageList.html", tag="message", tagaction="sends")

@Message.route('/message/messages/oneday_page')
def StatisticOneDay():
    return render_template("message/messageList.html", tag="message", tagaction="oneday")
    pass

@Message.route('/message/messages/allday_page')
def StatisticAllDay():
    return render_template("message/messageList.html", tag="message", tagaction="allday")
    pass

