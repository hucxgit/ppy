from flask import render_template, redirect, url_for
from . import Message
@Message.route('/message/messages/sends')
def sendsMessage():
    return render_template("message/messageList.html", tag="message", tagaction="sends")

