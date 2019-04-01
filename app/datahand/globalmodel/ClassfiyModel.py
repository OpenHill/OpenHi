from app.models.DB.mainDB import Classify


class ClassfiyModel:
    classfiyModel = {"Name": None, "Url": None, "IfDom": None, "IfDomList": []}  # {"NAME":"/post/1"}

    def GetAllClassfiy(self):
        List = Classify.query.filter().all()
        for i in List:
            if not i.upcfid:
                classfiyModelCopy = self.classfiyModel.copy()
                datalist = []
                List2 = Classify.query.filter(Classify.upcfid == i.cfid).all()
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
                yield classfiyModelCopy

    def GetOneClassfiy(self):
        pass
