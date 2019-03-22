from flask import session
from ..models.DB.mainDB import DB
from ..models.DB.mainDB import Comment, Post, Classify


class NoLoginIndexData:
    dataDict = {
        "Classfiy": [],
        # "User": {"Name": None, "UserSettingUrl": None},  # 没登陆
        "ContentList": []

    }

    ClassfiyModel = {"Name": None, "Url": None, "IfDom": None, "IfDomList": []}  # {"NAME":"/post/1"}
    ContentListModel = {"Url": None, "Title": None, "Content": None, "Author": None, "Date": None, "CommentNum": None,"Img":None}

    def GetALlClassfiy(self):
        self.dataDict["Classfiy"].clear()
        List = Classify.query.filter().all()
        for i in List:
            if not i.upcfid:
                ClassfiyModelCopy = self.ClassfiyModel.copy()
                datalist = []
                List2 = Classify.query.filter(Classify.upcfid == i.cfid).all()
                if List2:
                    datadict = {}
                    for j in List2:
                        datadict["Name"] = j.cfname
                        datadict["Url"] = "classfiy/" + str(j.cfid)
                        datalist.append(datadict.copy())
                    ClassfiyModelCopy["IfDom"] = True
                else:
                    ClassfiyModelCopy["IfDom"] = False
                ClassfiyModelCopy["Name"] = i.cfname
                ClassfiyModelCopy["Url"] = "classfiy/" + str(i.cfid)
                ClassfiyModelCopy["IfDomList"] = datalist
                self.dataDict["Classfiy"].append(ClassfiyModelCopy)
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
    def Mian(self):
        self.GetALlClassfiy()

        return self.dataDict
