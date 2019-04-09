from flask import session
from ..models.DB.mainDB import DB
from ..models.DB.mainDB import Comment, Post, Classfiy, User
from app.datahand.globalmodel.ClassfiyModel import ClassfiyModel
from app.datahand.globalmodel.UserModel import UserModel


class IndexData(ClassfiyModel, UserModel):
    def __init__(self, userId=None):
        self.userId = userId

    dataDict = {
        "Classfiy": None,
        "User": None,
        "ContentList": []

    }

    ContentListModel = {"Url": None, "Title": None, "Content": None, "Author": None, "Date": None, "CommentNum": None,
                        "Img": None}


    def GetAllContent(self):
        self.dataDict["ContentList"].clear()
        List = Post.query.filter().all()
        for i in List:
            ContentListModelCopy = self.ContentListModel.copy()
            ContentListModelCopy["Url"] = "/post/" + str(i.pid)
            ContentListModelCopy["Title"] = i.title
            ContentListModelCopy["Content"] = i.content[:200]
            ContentListModelCopy["Author"] = i.uid
            ContentListModelCopy["Img"] = i.img
            ContentListModelCopy["Data"] = i.insdate
            ContentListModelCopy["CommentNum"] = i.chacknum
            self.dataDict["ContentList"].append(ContentListModelCopy)

    def Main(self):
        self.dataDict["Classfiy"] = self.GetAllClassfiy()
        if self.userId:
            self.dataDict["User"] = self.GetOneUser()
        return self.dataDict
