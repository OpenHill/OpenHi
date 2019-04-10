from app.datahand.globalmodel.UserModel import UserModel
from app.datahand.globalmodel.ClassfiyModel import ClassfiyModel


class NavOkLoginModel(UserModel, ClassfiyModel):
    def __init__(self, userId):
        self.userId = userId

    dictData = {"Classfiy": None,
                "User": None, }

    def Main(self):
        self.dictData["Classfiy"] =self.GetAllClassfiy()
        self.dictData["User"] = self.GetOneUser()
        return self.dictData
