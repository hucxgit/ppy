# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import urllib2
from . import JsonFormat
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers
import os,time

class HttpUtil:
    @staticmethod
    def post(url,parameter):
        return HttpUtil.realpPost(url,parameter)
        pass
    @staticmethod
    def postNoData(url):
        return HttpUtil.realPostNoData(url)
        pass

    @staticmethod
    def get(url):
        pass



    #upload head
    #/images/uploadHead
    #file smallfile uid
    #http://139.196.35.198:8081/head/{uid}%100/{uid}.png
    #http://139.196.35.198:8081/head/{uid}%100/{uid}_s.png

    @staticmethod
    def uploadHeadFile():
        pass

    #/images/uploadBanner
    #file smallfile bannerId
    #http://139.196.35.198:8081/banner/{bannerId}%100/{bannerId}.png
    #http://139.196.35.198:8081/banner/{bannerId}%100/{bannerId}_s.png
    @staticmethod
    def uploadBannerFile():
        pass


    #/images/uploadCategory
    #file categoryId
    #http://139.196.35.198:8081/category/{categoryId}%100/{ categoryId}.png
    #http://139.196.35.198:8081/category /{ categoryId }%100/{ categoryId }_s.png
    @staticmethod
    def uploadCategoryFile():
        pass


    #/images/uploadPostImg
    #file1 smallfile1 file2 smallfile2
    @staticmethod
    def uploadPostFile():
        pass


    #/images/getImgHost
    #curl -l -H "Content-type: application/json" -X POST http://123.57.137.10:8080/images/getImgHost



    @staticmethod
    def realpPost(url, data):
        # 1
        data = JsonFormat.MyEncoder().encode(data)
        req = urllib2.Request(url, data=data)
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        res = urllib2.urlopen(req)
        return res.read()
    @staticmethod
    def realPostNoData(url):
        req = urllib2.Request(url)
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        res = urllib2.urlopen(req)
        return res.read()


    @staticmethod
    def commonUploadFile(url,file,id):
        boundary = '----------%s' % hex(int(time.time() * 1000))
        data = []
        data.append('--%s' % boundary)

        data.append('Content-Disposition: form-data; name="%s"\r\n' % 'username')
        data.append('jack')
        data.append('--%s' % boundary)

        data.append('Content-Disposition: form-data; name="%s"\r\n' % 'bannerId')
        data.append(id)
        data.append('--%s' % boundary)

        image_path = "/Users/hucx/Desktop/hello/400x400.png"
        fr = open(image_path, "rb")
        data.append('Content-Disposition: form-data; name="%s"; filename="400x400.png"' % 'profile')
        data.append('Content-Type: %s\r\n' % 'image/png')
        data.append(fr.read())
        fr.close()
        data.append('--%s--\r\n' % boundary)

        http_url = url
        http_body = '\r\n'.join(data)
        try:
            # buld http request
            req = urllib2.Request(http_url, data=data)
            # header
            req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
            req.add_header('User-Agent', 'Mozilla/5.0')
            #req.add_header('Referer', 'http://remotserver.com/')
            # post data to server
            resp = urllib2.urlopen(req, timeout=50)
            # get response
            qrcont = resp.read()
            print ("upload result")
            print qrcont


        except Exception, e:
            print 'http error'

    @staticmethod
    def uploadFile(url,path,spath,key,id):
        # 在 urllib2 上注册 http 流处理句柄
        print ("1111<<<")
        register_openers()
        print ("22222<<<")
        # 开始对文件 "DSC0001.jpg" 的 multiart/form-data 编码
        # "image1" 是参数的名字，一般通过 HTML 中的 <input> 标签的 name 参数设置

        # headers 包含必须的 Content-Type 和 Content-Length
        # datagen 是一个生成器对象，返回编码过后的参数
        #datagen, headers = multipart_encode({"file":f.stream,"smallfile":f.stream,"bannerId":id})

        #image_path = "/Users/hucx/Desktop/hello/400x400.png"
        fr = open(path, "rb")
        #image_path1="/Users/hucx/Desktop/hello/01.jpg"
        fr1=open(spath, "rb")
        params = {'file': fr,"smallfile":fr1,key: id}
        datagen, headers = multipart_encode(params)

        print ("=====")
        print (datagen)
        print (headers)
        # 创建请求对象
        request = urllib2.Request(url, datagen, headers)
        response_data = urllib2.urlopen(request)
        result = response_data.read()
        return result
