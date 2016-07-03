#from  flask_login import UserMixin,session
#from ppy import login_manager

class ResponseResult:
    def __init__(self,respDesc,respCode):
        self.respDesc = respDesc
        self.respCode = respCode
        pass
    def __del__(self):
        pass
class Result:
    def __init__(self, code, data, msg):
        self.code = code
        self.data = data
        self.msg = msg

    def __del__(self):
        pass


class User():
    def __init__(self, id, name, age):
        print('I\'m init')
        self.id = id
        self.name = name
        self.age = age


    def __del__(self):


        print('I\'m User del')

# @login_manager.user_loader
# def load_user(user_id):
#     print("login_manager.user_loader")
#     #print(user_id)
#     #user = User(100, "admin", "admin")
#     return  session['objects']


class Report:
    def __init__(self, reportId, reportUserName, categoryType, reportType, reportContent, reportReason,
                 reportTime):
        print('I\'m init')
        self.reportId = reportId
        self.reportUserName = reportUserName
        self.categoryType = categoryType
        self.reportType = reportType
        self.reportContent = reportContent
        self.reportReason = reportReason
        self.reportTime = reportTime

    def __del__(self):
        print('I\'m  Report del')


class Adviertisement:
    def __init__(self, adTitle, adUrl, adPlace, adTime, adState):
        print('I\'m init')
        self.adTitle = adTitle
        self.adUrl = adUrl
        self.adPlace = adPlace
        self.adTime = adTime
        self.adState = adState

    def __del__(self):
        print('I\'m  Report del')

class Banner:
    def __init__(self,bannerId,bannerName,bannerUrl,imageUrl,bannerIsDelete,created):
        self.bannerId = bannerId
        self.bannerName = bannerName
        self.bannerUrl = bannerUrl
        self.imageUrl = imageUrl
        self.bannerIsDelete = bannerIsDelete
        self.created = created
        pass
    def __del__(self):
        pass

class Article:
    def __init__(self,articleId,articleTitle,top,articleTime,articleState):
        self.articleId = articleId
        self.articleTitle = articleTitle
        self.top = top
        self.articleTime = articleTime
        self.articleState = articleState
        pass

    def __del__(self):
         pass



class MainCate:
    def __init__(self,categoryId,name,imageUrl,isDelete,parentId,created):
        self.categoryId = categoryId
        self.name = name
        self.imageUrl = imageUrl
        self.isDelete = isDelete
        self.parentId = parentId
        self.created = created
        pass
    def __del__(self):
        pass

class ForumCate:
    def __init__(self,forumcateId,forumcateName,forumcatePic,forumcateState):
        self.forumcateId = forumcateId
        self.forumcateName = forumcateName
        self.forumcatePic = forumcatePic
        self.forumcateState = forumcateState
        pass
    def __del__(self):
        pass


class AnonyCate:
        def __init__(self, anonyId, anonyName, anonyPic, anonyState):
            self.anonyId = anonyId
            self.anonyName = anonyName
            self.anonyPic = anonyPic
            self.anonyState = anonyState
            pass

        def __del__(self):
            pass


class InviteModel:
        def __init__(self,nickName,mobile,sums):
            self.nickName= nickName
            self.mobile = mobile
            self.sums = sums
            pass
        def __del__(self):
            pass

