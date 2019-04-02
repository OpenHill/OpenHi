from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Length, Email


class LoginFormVal(FlaskForm):
    username = StringField(
        label="邮箱",
        validators=[
            DataRequired(message="邮箱不能为空"),
            Length(min=7, max=50, message="账号长度为7-50"),
            Email(message="账号应为E-Mail格式")
        ],
        description="邮箱",
        render_kw={
            "id": "login_username",
            "class": "form-control",
            "placeholder": "请输入邮箱!",
            "required": 'required'  # 表示输入框不能为空，并有提示信息
        }
    )
    userpwd = PasswordField(
        label="密码",
        validators=[
            DataRequired(message="密码不能为空"),
            Length(min=6, max=20, message="密码长度为6-20"),
        ],
        description="密码",

        render_kw={
            "id": "login_userpwd",
            "class": "form-control",
            "placeholder": "请输入密码!",
            "required": 'required'

        }
    )

    submit = SubmitField(
        label="登QAQ录",
        render_kw={
            "type": "submit",
            "class": "btn btn-primary",
            "id": "login_submit"
        })


class RegninFormVal(FlaskForm):
    usernikename = StringField(
        label="昵称",
        validators=[
            DataRequired(message="昵称不能为空"),
            Length(min=1, max=10, message="昵称最多10个字符"),
        ],
        description="昵称",
        render_kw={
            "id": "regnin_usernikename",
            "class": "form-control",
            "placeholder": "请输入昵称",
            "required": 'required'  # 表示输入框不能为空，并有提示信息
        }
    )

    username = StringField(
        label="邮箱",
        validators=[
            DataRequired(message="邮箱不能为空"),
            Length(min=7, max=50, message="账号长度为7-50"),
            Email(message="账号应为E-Mail格式")
        ],
        description="邮箱",
        render_kw={
            "id": "regnin_username",
            "class": "form-control",
            "placeholder": "请输入邮箱!",
            "required": 'required'  # 表示输入框不能为空，并有提示信息
        }
    )
    userpwd = PasswordField(
        label="密码",
        validators=[
            DataRequired(message="密码不能为空"),
            Length(min=6, max=20, message="密码长度为6-20"),
        ],
        description="密码",
        render_kw={
            "id": "regnin_userpwd",
            "class": "form-control",
            "placeholder": "请输入密码!",
            "required": 'required'

        }
    )

    submit = SubmitField(
        label="注QAQ册",
        render_kw={
            "type": "submit",
            "class": "btn btn-primary",
            "id": "regnin_submit"
        })
