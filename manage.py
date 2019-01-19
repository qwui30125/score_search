# coding:utf-8

from isearch import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# 创建flask的应用对象
# app = create_app()

manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    print(app.url_map)
    manager.run()