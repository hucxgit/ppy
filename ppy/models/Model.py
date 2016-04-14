class Result:
    def __init__(self, code, data, msg):
        self.code = code
        self.data = data
        self.msg = msg

    def __del__(self):
        pass


class User:
    def __init__(self, id, name, age):
        print('I\'m init')
        self.id = id
        self.name = name
        self.age = age

    def __del__(self):
        print('I\'m User del')


class Report:
    def __init__(self, reportId, reportUserName, reportType, reportContentType, reportContent, reportReason,
                 reportTime):
        print('I\'m init')
        self.reportId = reportId
        self.reportUserName = reportUserName
        self.reportType = reportType
        self.reportContentType = reportContentType
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
    def __init__(self,bannerName,bannerUrl,bannerPic,bannerState):
        self.bannerName = bannerName
        self.bannerUrl = bannerUrl
        self.bannerPic = bannerPic
        self.bannerState = bannerState
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
    def __init__(self,maincateId,maincateTitle,maincatePic,maincateState):
        self.maincateId = maincateId
        self.maincateTitle = maincateTitle
        self.maincatePic = maincatePic
        self.maincateState = maincateState
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
