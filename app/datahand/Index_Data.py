from flask import session
from ..models.DB.mainDB import DB
from ..models.DB.mainDB import Comment, Post, Classfiy, User
from app.datahand.globalmodel.ClassfiyModel import ClassfiyModel
from app.datahand.globalmodel.UserModel import UserModel
from app.datahand.globalmodel.PostModel import PostModel


class IndexData(ClassfiyModel, UserModel, PostModel):
    def __init__(self, userId=None):
        self.userId = userId

    dataDict = {
        "Classfiy": None,
        "User": None,
        "ContentList": []

    }

    ContentListModel = {"Url": None, "Title": None, "Content": None, "Author": None, "Date": None, "CommentNum": None,
                        "Img": None}

    def Main(self):
        self.dataDict["Classfiy"] = self.GetAllClassfiy()
        if self.userId:
            self.dataDict["User"] = self.GetOneUser()
        self.dataDict["ContentList"] = self.getItemPostPage(1, 10)

        return self.dataDict
