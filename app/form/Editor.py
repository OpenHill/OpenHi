from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Length, Email


class EditorForm(FlaskForm):
    title = StringField(
        label="标题",
        validators=[
            DataRequired(message="标题不能为空"),
            Length(min=7, max=50, message="标题长度为7-50")
        ],
        description="标题",
        render_kw={
            "id": "post_title",
            "class": "form-control",
            "placeholder": "请输标题!",
        }
    )
    editor = StringField(
        label="文本编辑器",
        validators=[
            # DataRequired(message="编辑器不许为空"),
            # Length(min=20),
        ],
        description="编辑器",
        render_kw={
            "id": "editor_text",
            "class": "ckeditor",
            "style": "display:none;"
        }
    )

    submit = SubmitField(
        label="发布",
        render_kw={
            "type": "submit",
            "class": "btn btn-primary",
            "id": "post_submit"
        })
