import json
import logging
import logging.config
import os
import yaml
import ntpath
import shutil
import datetime
from flask import make_response, abort, request
from flask_restful import reqparse, abort, Api, Resource
from flask import make_response, abort, request, redirect, url_for, Flask
from werkzeug.utils import secure_filename
from google.cloud import storage
from config import db, basedir
from models.librarymodel import Library
from schemas.libraryschema import LibrarySchema
from schemas.templetschema import TemplateSchema
from schemas.userlibraryshema import LibraryUserSchema


CONFIG_PATH = os.path.join(basedir, 'loggeryaml/librarylogger.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('getpostlibrarys')
loggers = logging.getLogger("consolelibrarys")


app = Flask(__name__, static_url_path='/static')
path = os.getcwd()
UPLOAD_FOLDER = path+'/static'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class GetcreateLibrary(Resource):
    def __init__(self):
        pass

    def get(self):
        try:
            library = db.session.query(Library).order_by(Library.id).all()
            if library:
                library_schema = LibraryUserSchema(many=True)
                data = library_schema.dump(library).data
                logger.info("data feteched successfully")
                loggers.info("data feteched successfully")
                return({"success": True, "data": data})
            else:
                logger.warning("library data not found")
                loggers.warning("library data not found")
                return({"success": True, "data": []})
        except Exception as e:
            logger.warning(str(e))
            loggers.warning(str(e))
            return({"success": False, "message": str(e)})

    def post(self):
        # try:
            str_data = request.form["data"]
            da = json.loads(str_data)
            if "Template_Title" in da.keys():
                templateName = da["Template_Title"]
                del da["Template_Title"]
            # library_lastrecord = db.session.query(
            #     Library).order_by(Library.id.desc()).first()
            schema = LibrarySchema()
            time = str(datetime.datetime.now())
            ref = ''.join([n for n in time if n.isdigit()])
            totaldata = ""
            # if library_lastrecord:
            #     lastrecord = schema.dump(library_lastrecord).data
            #     Version_id = lastrecord["Libaray_Reference"]
            #     da.update({"Libaray_Reference": ref, "Version_id": Version_id})
            # else:
            da.update({"Libaray_Reference":ref})
            userId = da["createdby"]
            if da["Template"] == "0":
                new_library = schema.load(da, session=db.session).data
                db.session.add(new_library)
                db.session.commit()
                data = schema.dump(new_library).data
                totaldata = data
                logger.info("library data posted successfully")
                loggers.info("library data posted successfully")
            else:
                files = request.files.getlist("file")
                print("==================",files)
                # files_in_static_folder = os.listdir(basedir+"/static")
                # file_name = []
                # for f in files:
                #     file_name.append(f.filename)
                # check = [i for i in file_name if i in files_in_static_folder]
                # if check == []:
                new_library = schema.load(da, session=db.session).data
                db.session.add(new_library)
                db.session.commit()
                data = schema.dump(new_library).data
                totaldata = data
                library_id = data["id"]
                logger.info("library data posted successfully")
                loggers.info("library data posted successfully")
                try:
                    if data != {}:
                        # template_names = json.loads(templateName)
                        url_path = []
                        for name_files in files:
                            filename, file_extension = os.path.splitext(
                                name_files.filename)
                            time_date = str(datetime.datetime.now())
                            ref2 = ''.join([n for n in time_date if n.isdigit()])
                            fileextension = ref2+file_extension
                            # rename_file = os.rename(name_files.filename, ref)
                            filename = secure_filename(name_files.filename)
                            name_files.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                            os.rename(os.path.join(
                                app.config['UPLOAD_FOLDER'], filename), os.path.join(app.config['UPLOAD_FOLDER'], fileextension))
                            url_path.append(
                                url_for("static", filename=fileextension))
                        total_data = dict(zip(templateName, url_path))
                        for key,value in total_data.items():
                            template_dict = {
                                "Template_Title": key, "Template_File": value, "user_id": userId, "library_id": library_id}
                            template_schema = TemplateSchema()
                            new_template = template_schema.load(
                                template_dict, session=db.session).data
                            db.session.add(new_template)
                            db.session.commit()
                            temp_data = template_schema.dump(new_template).data
                            logger.info("template data posted successfully")
                            loggers.info("template data posted successfully")
                    else:
                        logger.info("Library not created")
                        loggers.info("Library not created")
                        return({"success":False,"message":"Library not created"})
                except Exception as e:
                    obj = db.session.query(Library).filter(
                        Library.id == library_id).first()
                    if obj:
                        db.session.delete(obj)
                        db.session.commit()
                        logger.info("succesffully deleted ")
                        loggers.info("data updated successfully baesd on id ")
                    return({"success": False, "message": str(e)})
                # else:
                #     logger.info("already file exists {}".format(check))
                #     loggers.info("already file exists {}".format(check))
                #     return ({"success":False,"message":"already file exists {}".format(check)})
            logger.info({"success": True, "data": totaldata})
            loggers.info({"success": True, "data": totaldata})
            return({"success": True, "data": totaldata})
        # except Exception as e:
        #     logger.warning(str(e))
        #     loggers.warning(str(e))
        #     return({"success": False, "message": str(e)})
