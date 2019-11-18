from models.usermodel import Users
from schemas.userschema import GetallUsersSchemas
from flask_restful import Resource, reqparse
from flask import request
import os
import datetime

from config import db, basedir
import logging
import logging.config
import yaml


CONFIG_PATH = os.path.join(basedir, 'loggeryaml/userlogger.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('getupdateusers')
loggers = logging.getLogger("consoleusers")


class Getallusers(Resource):
   def __init__(self):
       pass
   # Roles get call

   def get(self):
       try:
           user_obj = db.session.query(Users).order_by(Users.id).all()
           if user_obj:
               user_schema = GetallUsersSchemas(many=True)
               data = user_schema.dump(user_obj).data
               logger.info("data feteched successfully")
               loggers.info("data feteched successfully")
               return({"success": True, "data": data})
           else:
               logger.warning("users not found")
               loggers.warning("users not found")
               return({"success": False, "message": "users not found"})
       except Exception as e:
           logger.warning(str(e))
           loggers.warning(str(e))
           return({"success": False, "message": str(e)})
