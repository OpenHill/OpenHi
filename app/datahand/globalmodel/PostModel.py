from app.models.DB.mainDB import Post
from flask import url_for
import re


class PostModel:
    postModel = {"Url": None, "Title": None, "Content": None, "Author": None, "Date": None, "CommentNum": None,
                 "Img": None}

    postId = None

    def GetAllPost(self):
        postlist = Post.query.filter().all()
        for i in postlist:
            print()

    def getPostPage(self, pages=1, pagenum=10):
        #  绝对值
        pages = abs(pages if pages != 0 else 1)
        pagenum = abs(pagenum)

        # 查询

        postList = Post.query.filter().all()
        if (pages * pagenum < len(postList)):
            postList = postList[(pages - 1) * pagenum:pages * pagenum]
        else:
            postList = postList[(pages - 1) * pagenum:]

        if len(postList) == 0:
            return postList
        else:
            for index, i in enumerate(postList):
                postModelcopy = self.postModel.copy()

                # 内容处理
                cloesallhtml = re.compile(r'<[^>]+>', re.S)
                cloesimg = re.compile(r'<img.*?>', re.S)
                cloespre = re.compile(r'<pre([\s\S]*) *?</pre>', re.S)
                content = cloesimg.sub("*[图片]*", i.content)
                content = cloespre.sub("*[代码块]*", content)
                content = cloesallhtml.sub('', content)

                # 文章是否包含图片？
                imgs = re.findall(r'src="(.*?[\.png|\.jpg|\.gif|\.bmp|\.jpeg])"', i.content)


                postModelcopy["Url"] = "/post/" + str(i.pid)
                postModelcopy["Title"] = i.title
                postModelcopy["Content"] = content[:200]
                postModelcopy["Author"] = i.user.nikename
                postModelcopy["Img"] = imgs[0] if imgs else url_for("static", filename="img/bg.jpg")
                postModelcopy["Data"] = i.insdate
                postModelcopy["CommentNum"] = i.chacknum
                postList[index] = postModelcopy

            return postList
