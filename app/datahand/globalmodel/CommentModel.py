from app.models.DB.mainDB import Comment
from app.models.Model.CommentModels import CommentAllModel


class CommentModel:

    def getAllComment(self, pid):
        commentList = Comment.query.filter(Comment.pid == pid).all()

        Commetlist = []
        for i in commentList:
            if not i.upcid:
                img = None
                if i.uid:
                    img = i.user.img
                cam = CommentAllModel(
                    img=img,
                    uid=i.uid,
                    cid=i.cid,
                    userNikeName=None,
                    nikeName=i.nikename,
                    content=i.text,
                    domcomment=self.__getchildCommet(i.cid, commentList)
                )
                Commetlist.append(cam)

        return Commetlist

    def __getchildCommet(self, cid, data):
        childCommetlist = []
        for i in data:
            if i.upcid == cid:
                img = None
                if i.uid:
                    img = i.user.img
                cam = CommentAllModel(
                    img=img,
                    uid=i.uid,
                    cid=i.cid,
                    userNikeName=self.__getCidNikeName(i.relycid, data),
                    nikeName=i.nikename,
                    content=i.text.replace("\\n", ""),
                    domcomment=None
                )
                childCommetlist.append(cam)
        return childCommetlist

    def __getCidNikeName(self, relycid, data):
        for i in data:
            if i.cid == relycid:
                return i.nikename
