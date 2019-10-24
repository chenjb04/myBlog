from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import create_app, db

app = create_app('development')
manager = Manager(app)

# 将app和db关连
Migrate(app, db)
# 将数据库迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

