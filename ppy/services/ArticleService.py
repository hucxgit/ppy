from ..utils import JsonFormat
from ..models import Model

#ArticleService
class ArticleService:
    def __init__(self):
        pass
    def __del__(self):
        pass
    def serviceArticles(self,articleType):
        articles = []
        for num in range(0, 3 * articleType + 1):
            article = Model.Article(10,"title","hno","2015-11-06 12:41","1")
            articles.append(article)
        return JsonFormat.MyEncoder().encode({"code": 200, "data": articles, "msg": "success"})

