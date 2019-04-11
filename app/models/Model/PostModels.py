class IndexPostItemModel:
    def __init__(self, url, title, content, author, date, commentNum, img,flag):
        self.url = url
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        self.commentNum = commentNum
        self.img = img
        self.flag = flag


class PostShowPageModel:
    def __init__(self, pid, author, title, content, chacknum, cfid, insdate, update, flag):
        self.pid = pid
        self.author = author
        self.title = title
        self.content = content
        self.chacknum = chacknum
        self.cfid = cfid
        self.insdate = insdate
        self.update = update
        self.flag = flag
