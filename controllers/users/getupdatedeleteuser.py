from models.usermodel import Users
from schemas.userschema import UsersGetSchema,UsersSchema
from config import db
from flask_restful import Resource, reqparse
from flask import request
from sqlalchemy import func
import os
import datetime
from models.rolemodel import Roles


from config import db,basedir
import logging, logging.config, yaml


CONFIG_PATH = os.path.join(basedir,'loggeryaml/userlogger.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH),Loader=yaml.FullLoader))
logger = logging.getLogger('getupdateusers')
loggers = logging.getLogger("consoleusers")





class GetUpdateUser(Resource):
    def __init__(self):
        pass
    def get(self,id):
        try:
            user = Users.query.filter(Users.id == id).one_or_none()
            if user is not None:
                user_schema = UsersGetSchema()
                data = user_schema.dump(user).data
                logger.info("data feteched successfully")
                loggers.info("data feteched successfully")
                return({"success":True,"data":data})
            else:
                logger.warning("user not found")
                logger.warning("user not found")
                return({"success":False,"message": "user not found"})
        except Exception as e:
            logger.warning(str(e))
            logger.warning(str(e))
            return({"success":False,"message":str(e)})



    # call to update the user details based on user_id

    def put(self,id):
        try:
            da = request.get_json()
            da.update({"updated_at": datetime.datetime.utcnow()})
            user = db.session.query(Users).filter_by(id = id).update(da)
            if user:
                db.session.commit()
                user_obj = Users.query.filter(Users.id == id).one()
                user_schema = UsersSchema()
                data = user_schema.dump(user_obj).data
                logger.info("data updated successfully")
                loggers.info("data updated successfully")
                return({"success":True,"data":data})
            else:
                logger.warning("user not updated")
                loggers.warning("user not updated")
                return({"success":False,"message": "user not updated "})
        except Exception as e:
            logger.warning(str(e))
            loggers.warning(str(e))
            return({"success":False,"message":str(e)})



    def delete(self,id):
        try:
            obj=db.session.query(Users).filter(Users.id==id).first()
            if obj:
                db.session.delete(obj)
                db.session.commit()
                logger.info("Users deleted successfully")
                loggers.info("Users deleted successfully")
                return("Users deleted successfully")
            else:
                logger.warning("user doesnot deleted")
                loggers.warning("user doesnot deleted")
                return({"success":False,"message": "user doesnot deleted"})
        except Exception as e:
            logger.warning(str(e))
            loggers.warning(str(e))
            return({"success":False,"message":str(e)})
