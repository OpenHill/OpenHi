from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length, Email


class EditorForm(FlaskForm):
    postTitle = StringField(
        label="标题",
        validators=[
            DataRequired(message="标题不能为空"),
            Length(min=7, max=50, message="标题长度为7-50")
        ]

    )
    postContent = StringField(
        label="文本编辑器",
        validators=[
            DataRequired(message="编辑器不许为空"),
            Length(min=20, max=30000, message="30～30000字"),
        ]

    )

    postclassfiy = StringField(
        label="分类",
        validators=[
            DataRequired(message="不能为空"),
            Length(min=1, max=2)
        ]
    )
