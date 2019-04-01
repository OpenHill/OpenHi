from app.models.DB.mainDB import Post


class PostModel:
    postModel = {"Pid": None, "Uid": None, "UName": None}
    postId = None

    def GetAllPost(self):
        postlist = Post.query.filter().all()
