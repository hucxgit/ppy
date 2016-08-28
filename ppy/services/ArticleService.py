# -*- coding:utf-8 -*-
from ..utils import JsonFormat
from ..models import Model
from ppy import getConfigByKey
from ..utils import HttpUtil

#ArticleService
class ArticleService:
    def __init__(self):
        pass
    def __del__(self):
        pass
    def serviceArticles(self,categoryId):

        print(categoryId)
        posturl = getConfigByKey("URL") + ":" + getConfigByKey("PORT") + "/post/queryByCid"
        print(posturl)
        data = {"categoryId": categoryId, "pageSize": 1000,"pageNo":0}
        result = HttpUtil.post(posturl, data)

        print("===============ArticleService service list 1 ====================");
        print(result)
        print(type(result))
        r = JsonFormat.MyDecoder().decode(result)
        print(r)
        print(type(r))
        print("===============ArticleService service list 2 ====================");
        code = r["respCode"]
        msg = r["respDesc"]

        postinfos = []


        for obj in r["post"]:
            pInfo = obj["postInfo"]
            pContent = obj["context"]
            postinfo = Model.PostInfo(pInfo["postId"],pInfo["uid"],pInfo["author"],pInfo["title"],pInfo["simpleContent"]
                                      ,pContent["content"])

            postinfos.append(postinfo)
        return JsonFormat.MyEncoder().encode({"code": code, "data": postinfos, "msg": msg})



    #根据postid 查询帖子详情
    def serviceArticleDetail(self,postid):
        print(postid)
        posturl = getConfigByKey("URL") + ":" + getConfigByKey("PORT") + "/post/queryByPostid"
        print(posturl)
        data = {"postId": postid, "uid": 1}
        result = HttpUtil.post(posturl, data)

        print("===============ArticleService serviceArticleDetail list 1 ====================");
        print(result)
        print(type(result))
        r = JsonFormat.MyDecoder().decode(result)
        print(r)
        print(type(r))
        print("===============ArticleService serviceArticleDetail list 2 ====================");
        code = r["respCode"]
        msg = r["respDesc"]

        obj = r["post"];
        if len(obj) == 1:
            obj = obj[0]
            pInfo = obj["postInfo"]
            pContent = obj["context"]
            postinfo = Model.PostInfo(pInfo["postId"], pInfo["uid"], pInfo["author"], pInfo["title"],
                                      pInfo["simpleContent"]
                                      , pContent["content"])

            result = JsonFormat.MyEncoder().encode({"code": code, "msg": msg, "data": postinfo})
            return result
        else:
            return JsonFormat.MyEncoder().encode({"code": code, "msg": msg})


    def serviceCreatePost(self,uid,categoryId,author,title,articlePic,simpleContent,content):
        posturl = getConfigByKey("URL") + ":" + getConfigByKey("PORT") + "/post/create"
        print(posturl)
        data = {"uid":uid,"categoryId":categoryId,
                "author": author,
                "title": title,
                "simpleContent": simpleContent, "context": content,
                 "images":[articlePic]}
        result = HttpUtil.post(posturl, data)
        return result

    #更新帖子
    def serviceUpdatePost(self,postId,categoryId,author,title,simpleContent,content):
        posturl = getConfigByKey("URL") + ":" + getConfigByKey("PORT") + "/post/updatePostinfo"
        print(posturl)
        data = {"postId": postId,"categoryId":categoryId, "author": author,"title":title,"simpleContent":simpleContent,"context":content}
        result = HttpUtil.post(posturl, data)

        print("===============ArticleService serviceUpdatePost list 1 ====================");
        print(result)
        print(type(result))
        r = JsonFormat.MyDecoder().decode(result)
        print(r)
        print(type(r))
        print("===============ArticleService serviceUpdatePost list 2 ====================");

        code = r["respCode"]
        msg = r["respDesc"]
        return JsonFormat.MyEncoder().encode({"code": code, "msg": msg})
        pass

    #删除帖子
    def serviceDeletePostById(self,postid):
        posturl = getConfigByKey("URL") + ":" + getConfigByKey("PORT") + "/post/delete"
        print(posturl)
        data = {"postId": postid}
        result = HttpUtil.post(posturl, data)

        print("===============ArticleService serviceDeletePostById list 1 ====================");
        print(result)
        print(type(result))
        r = JsonFormat.MyDecoder().decode(result)
        print(r)
        print(type(r))
        print("===============ArticleService serviceDeletePostById list 2 ====================");

        code = r["respCode"]
        msg = r["respDesc"]
        return JsonFormat.MyEncoder().encode({"code": code, "msg": msg})
        pass
