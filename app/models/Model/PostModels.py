class IndexPostItemModel:
    def __init__(self, url, title, content, author, date, commentNum, img, flag):
        self.url = url
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        self.commentNum = commentNum
        self.img = img
        self.flag = flag


class PostShowPageModel:
    def __init__(self, pid, author, uid, title, content, chacknum, classfiyname, insdate, update, flag, tags):
        self.pid = pid
        self.author = author
        self.uid = uid
        self.title = title
        self.content = content
        self.chacknum = chacknum
        self.classfiyname = classfiyname
        self.insdate = insdate
        self.update = update
        self.flag = flag
        self.tags = tags
