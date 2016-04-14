#ppyWeb
#pip freeze >> requirements.txt

1:stepone new create virtualenv
sudo pip install virtualenv
virtualenv --distribute ENV
cd ENV/
source bin/activate


2:install dependency
pip install -r requirements.txt 
or 
pip install -U -r requirements.txt

3:run server
python manager.py dev




#delete remote file
git rm -r --cached .Python
git commit -am "删除多余文件"
git push origin master

//reportlist
http://localhost:5001/reportlistHtml
//index
http://localhost:5001/indexHtml




//广告ad
ad/ads           adList.html adListContent.html   adActionContent.html
ad/ads/newad     adList.html
ad/ads/editad    adList.html
adlist newadd editadd
$<tag>=ads $<tagaction> newad editad


//banner
banner
banner/banners/<tag>                 mainbannerList.html mainbannerListContent.html mainbannerActionContent.html
banner/banners/<tag>/newbanner       mainbannerList.html
banner/banners/<tag>/editbanner      mainbannerList.html
$<tag>=mainbanner,forumbanner   $<tagaction> newbanner,editbanner






//发现
//主页分类
find/maincate                   mainCateList.html mainCateListContent.html  mainCateActionContent.html
find/maincate/newcate           mainCateList.html
find/maincate/editcate          mainCateList.html
$<tag>=maincate forumcate $<tagaction>newcate editcate


//论坛分类
find/forumcate                   forumCateList.html forumCateListContent.html forumCateActionContent.html
find/forumcate/newcate           forumCateList.html
find/forumcate/editcate          forumCateList.html
$<tag>=forumcate forumcate $<tagaction>newforumcate editforumcate subforumcate


//匿名管理
find/anony                         anonyList.html       anonyListContent.html anonyActionContent.html
find/anony/newanony                anonyList.html
find/anony/editanony               anonyList.html
$<tag>=annoy $<tagaction>newanony editanony

//文章
find/article                        articleList.html articleListContent.html articleActionContent.html
find/article/newarticle             articleList.html
find/article/editarticle            articleList.html
$<tag>=article $<tagaction>newarticle editarticle

//report
report/reports   reportlist.html