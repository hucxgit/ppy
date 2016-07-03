from flask import request,redirect,url_for

from . import Message
from ppy import services


# sendMessages
@Message.route('/sendMessages',methods=['POST'])
def sendMessages():
    if request.method == 'POST':
        print("hello sendMessage")
        print (request.form)
        title = request.form['messageTitle']
        content = request.form['messageContent']
        url = request.form['messageUrl']
        imageUrl = request.form['messageImageUrl']

        dic = services.MessageService().serviceSendMessages(title,content,url,imageUrl)
        if dic['respCode'] == "000000":
            return "success"
        else:
            return "failure"


@Message.route('/oneday')
def statictisOneDay():
    return services.MessageService().serviceStatictis("day")

@Message.route('/allday')
def statictisallDay():
    return services.MessageService().serviceStatictis("all")


