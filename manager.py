import os
from flask_restful import Api
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import db, app
from models.rolemodel import Roles
from models.usermodel import Users
from models.librarymodel import Library
from models.templatemodel import Templates
# os.environ['APP_SETTINGS'] = 'config.DevelopmentConfig'
migrate = Migrate(app, db)

app.app_context().push()
db.create_all(app=app)
db.session.commit()
db.init_app(app)


manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()
    
    
