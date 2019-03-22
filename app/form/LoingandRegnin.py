from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, ValidationError, NumberRange


class LoginFormVal(FlaskForm):
    username = StringField(
        label="账号",
        validators=[
            DataRequired("请输入用户名"),
            NumberRange(7, 20)
        ],
        description="账号",
        render_kw={
            "id": "login_username",
            "class": "form-control",
            "placeholder": "请输入账号!",
            "required": 'required'  # 表示输入框不能为空，并有提示信息
        }
    )
    userpwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("请输入密码")
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
        label="登录",
        render_kw={
            "type": "submit",
            "class": "btn btn-primary",
            "id": "login_submit"
        })
