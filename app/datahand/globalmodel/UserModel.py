from app.models.DB.mainDB import User


class UserModel:
    userModel = {"Uid": None, "Name": None, "Email": None, "Img": None, "Statement": None}
    userId = None

    def GetAllUser(self):
        pass

    def GetOneUser(self):
        UserObj = User.query.filter(User.uid == self.userId).first()
        userModelCopy = self.userModel.copy()
        userModelCopy["Uid"] = UserObj.uid
        userModelCopy["Name"] = UserObj.nikename
        userModelCopy["Email"] = UserObj.email
        userModelCopy["Img"] = UserObj.img
        userModelCopy["Statement"] = UserObj.statement
        return userModelCopy

    # def get