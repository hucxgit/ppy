from ..utils import JsonFormat
import urllib2
import urllib
import types
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


        posturl = "http://139.196.35.198:8080/message/sends"
        #posturl = "http://127.0.0.1:8080/message/sends"
        data = {"messageType":1,"sendId":-1,"messageTitle":messageTitle,"messageContent":messageContent,"messageImg":messageImageUrl,"messageUrl":messageUrl}
        result = post(posturl, data)
        print("result")
        print(result)
        print(type(result))
        r = JsonFormat.MyDecoder().decode(result)
        print(r)
        print(type(r))
        return r
#post request
def post(url, data):
    #1
    data = JsonFormat.MyEncoder().encode(data)
    print(data);
    req = urllib2.Request(url,data=data)
    print(req)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    res = urllib2.urlopen(req)
    return res.read()




    #2
    # test_data = urllib.urlencode(data)
    #
    # #req = urllib2.Request(url, data=test_data)
    # res = urllib2.urlopen(url,test_data)
    # print(res)
    # print(res.read())
    # return "hello"


    #return  "hello"





    #enable cookie
    # opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
    # response = opener.open(req,data)
    # return response.read()