from app import create_app
from Config import Config

# 写在 __main__ 里不能导入
app = create_app(Config)

if __name__ == '__main__':
    app.run(host=Config.HOST)
