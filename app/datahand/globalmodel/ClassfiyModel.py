from app.models.DB.mainDB import Classfiy


class ClassfiyModel:
    classfiyModel = {"Name": None, "Url": None, "IfDom": None, "IfDomList": []}  # {"NAME":"/post/1"}
    aFatherClassfiyModel = {"Id": None, "Name": None, "upId": None}

    def GetAllClassfiy(self):
        List = Classfiy.query.filter().all()
        allClassfiyList = []
        for i in List:
            if not i.upcfid:
                classfiyModelCopy = self.classfiyModel.copy()
                datalist = []
                List2 = Classfiy.query.filter(Classfiy.upcfid == i.cfid).all()
                if List2:
                    datadict = {}
                    for j in List2:
                        datadict["Name"] = j.cfname
                        datadict["Url"] = "classfiy/" + str(j.cfid)
                        datalist.append(datadict.copy())
                    classfiyModelCopy["IfDom"] = True
                else:
                    classfiyModelCopy["IfDom"] = False
                classfiyModelCopy["Name"] = i.cfname
                classfiyModelCopy["Url"] = "classfiy/" + str(i.cfid)
                classfiyModelCopy["IfDomList"] = datalist
                allClassfiyList.append(classfiyModelCopy)
        return allClassfiyList

    def GetOneClassfiy(self):
        pass

    def getFatherClassfiy(self) -> list:
        """
        返回所有父级分类
        :return: list[dict]
        """
        list = Classfiy.query.filter(Classfiy.upcfid == None).all()
        aFatherClassfiyModelList = []
        for i in list:
            aFatherClassfiyModelCopy = self.aFatherClassfiyModel.copy()
            aFatherClassfiyModelCopy["Id"] = i.cfid
            aFatherClassfiyModelCopy["Name"] = i.cfname
            aFatherClassfiyModelCopy["upId"] = i.upcfid
            aFatherClassfiyModelList.append(aFatherClassfiyModelCopy)
        return aFatherClassfiyModelList

    def getChildrenClassfiy(self, id) -> list:
        """
        查询子分类
        :param id: 父级ID
        :return: dict
        """
        list = Classfiy.query.filter(Classfiy.upcfid == id).all()
        aChildrenClassfiyModelList = []
        for i in list:
            aChildrenClassfiyModelCopy = self.aFatherClassfiyModel.copy()
            aChildrenClassfiyModelCopy["Id"] = i.cfid
            aChildrenClassfiyModelCopy["Name"] = i.cfname
            aChildrenClassfiyModelCopy["upId"] = i.upcfid
            aChildrenClassfiyModelList.append(aChildrenClassfiyModelCopy)
        return aChildrenClassfiyModelList
