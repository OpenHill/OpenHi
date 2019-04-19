from app.models.DB.mainDB import Post
from app.models.Model.PostModels import IndexPostItemModel, PostShowPageModel
from flask import url_for
import re


class PostModel:
    postId = None

    def getItemPostPage(self, pages=1, pagenum=10) -> list:
        """
        获取首页的展示项
        :param pages: 第几页
        :param pagenum: 一页多少项
        :return: 包含pagenum个项的list
        """
        #  绝对值
        pages = abs(pages if pages != 0 else 1)
        pagenum = abs(pagenum)

        # 查询
        postList = Post.query.filter(Post.flag !=0).all()

        if (pages * pagenum < len(postList)):
            postList = postList[(pages - 1) * pagenum:pages * pagenum]
        else:
            postList = postList[(pages - 1) * pagenum:]

        if len(postList) == 0:
            return postList
        else:
            for index, i in enumerate(postList):
                # 内容处理
                cloesallhtml = re.compile(r'<[^>]+>', re.S)
                cloesimg = re.compile(r'<img.*?>', re.S)
                cloespre = re.compile(r'<pre([\s\S]*) *?</pre>', re.S)
                content = cloesimg.sub("*[图片]*", i.content)
                content = cloespre.sub("*[代码块]*", content)
                content = cloesallhtml.sub('', content)

                # 文章是否包含图片？
                imgs = re.findall(r'src="(.*?[\.png|\.jpg|\.gif|\.bmp|\.jpeg])"', i.content)
                item = IndexPostItemModel(
                    url="/post?pid=" + str(i.pid),
                    title=i.title,
                    content=content[:200],
                    author=i.user.nikename,
                    date=i.insdate,
                    img=imgs[0] if imgs else url_for("static", filename="img/bg.jpg"),
                    commentNum=i.chacknum,
                    flag=i.flag == 1
                )

                postList[index] = item.__dict__
            return postList

    def getPost(self, pid):
        postdict = Post.query.filter(Post.pid == pid).first()

        if postdict:
            postPageData = PostShowPageModel(
                pid=postdict.pid,
                author=postdict.user.nikename,
                uid=postdict.user.uid,
                title=postdict.title,
                content=postdict.content,
                chacknum=postdict.chacknum,
                classfiyname=postdict.classfiy.cfname,
                insdate=str(postdict.insdate)[:11],
                update=str(postdict.update)[:11],
                flag=postdict.flag,
                tags=[i.name for i in postdict.tag]
            )
            return postPageData
        else:
            return postdict

    def getPostByUid(self, uid):
        postdictlist = Post.query.filter(Post.uid == uid , Post.flag != 0).all()

        for index, postdict in enumerate(postdictlist):
            if postdict:
                postPageData = PostShowPageModel(
                    pid=postdict.pid,
                    author=postdict.user.nikename,
                    uid=postdict.user.uid,
                    title=postdict.title,
                    content=postdict.content,
                    chacknum=postdict.chacknum,
                    classfiyname=postdict.classfiy.cfname,
                    insdate=postdict.insdate,
                    update=postdict.update,
                    flag=postdict.flag,
                    tags=[i.name for i in postdict.tag]
                )
                postdictlist[index] = postPageData
            return postdictlist
