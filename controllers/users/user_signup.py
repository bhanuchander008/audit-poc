from models.usermodel import Users
from schemas.userschema import user_signupSchema
from config import *
from flask import request, make_response, jsonify
from flask_restful import Resource
from werkzeug.security import generate_password_hash
import os
from config import db,basedir
import logging, logging.config, yaml
from sqlalchemy import func
from models.rolemodel import Roles


CONFIG_PATH = os.path.join(basedir,'loggeryaml/userlogger.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH),Loader=yaml.FullLoader))
logger = logging.getLogger('signin_users')
loggers = logging.getLogger("consoleusers")



class Signup(Resource):
    def __init__(self):
        pass

    def get(self):
        try:
            user = db.session.query(Users).filter(Users.roleId==4).order_by(Users.id).all()
            order_count = (db.session.query(Users, func.count(Orders.id).label("num_orders")) .outerjoin(Orders, Users.order).filter(Users.roleId==4).group_by(Users.id))
            total_orders = {b.id:count for b,count in order_count}
            total_amount = (db.session.query(Users, func.sum(Orders.finalPrice).label("total_amount")) .outerjoin(Orders, Users.order).filter(Users.roleId==4).group_by(Users.id))
            user_amount  =  {b.id:total for b,total in total_amount}
            address_count = (db.session.query(Users, func.count(Addresses.id).label("num_address")) .outerjoin(Addresses, Users.address).filter(Users.roleId==4).group_by(Users.id))
            user_address = {b.id:count for b,count in address_count}

            if user:
                user_schema = UsercountSchema(many = True)
                data = user_schema.dump(user).data
                logger.info("data feteched successfully")
                loggers.info("data feteched successfully")
                return({"success":True,"data":data,"total_orders":total_orders,"user_amount":user_amount,"user_address":user_address})
            else:
                logger.warning("user not found")
                loggers.warning("user not found")
                return({"success":False,"message": "user not found"})
        except Exception as e:
            logger.warning(str(e))
            loggers.warning(str(e))
            return({"success":False,"message":str(e)})


    def post(self):
        try:
            post_user = request.get_json()
            email = post_user['email']
            firstName = post_user['first_name']
            lastName = post_user['last_name']
            password = post_user['password']
            phone = post_user["phone"]
            dict = {"first_name": firstName, "last_name": lastName, "email": email, "password": password, "phone":phone}
            email_id  = db.session.query(Users).filter(Users.email == email).first()
            if email_id is None:
                hash_password = generate_password_hash(password)
                schema = user_signupSchema()
                new_signup = schema.load(dict, session = db.session).data
                new_signup.password = hash_password
                db.session.add(new_signup)
                db.session.commit()
                data = schema.dump(new_signup).data
                logger.info("user signup successfully")
                loggers.info("user signup successfully")
                return {'success':True,
                    'data'         : data
                    }
            else:
                logger.warning("email already exists")
                loggers.warning("email already exists")
                return ({"success":False,"message":"email already exists"})
        except Exception as e:
            logger.warning(str(e))
            loggers.warning(str(e))
            return({"success":False,"message":str(e)})
