from models.usermodel import Users
from schemas.userschema import User_loginSchema
from flask_restful import Resource
from config import *
from flask import request,session
from werkzeug.security import check_password_hash
import datetime


from config import db,basedir
import logging, logging.config, yaml


CONFIG_PATH = os.path.join(basedir,'loggeryaml/userlogger.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH),Loader=yaml.FullLoader))
logger = logging.getLogger('signup_users')
loggers = logging.getLogger("consoleusers")


class Signin(Resource):
    def __init__(self):
        pass

    # login call for the user
    def post(self):
        try:
            sign_in = request.get_json()
            email = sign_in['email']
            password = sign_in['password']
            email_check = db.session.query(Users).filter(Users.email == email).first()
            if email_check is not None:
                schema = User_loginSchema()
                data   = schema.dump(email_check).data
                hashed_password = email_check.password
                if check_password_hash(hashed_password,password):
                    logger.info("user sigin successfully")
                    loggers.info("user sigin successfully")
                    return {"success":True,
                        'data':data,
                        'message': 'logined successfully'
                        }
                else:
                    logger.warning("Invalid password")
                    loggers.warning("Invalid password")
                    return({"success":False,"message": "Invalid password"})
            else:
                logger.warning("Invalid UserName")
                loggers.warning("Invalid UserName")
                return({"success":False,"message": "Invalid UserName"})
        except Exception as e:
            logger.warning(str(e))
            loggers.warning(str(e))
            return({"success":False,"message":str(e)})
