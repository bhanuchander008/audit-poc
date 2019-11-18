import logging
import logging.config
import os
import yaml
import json
import datetime
from flask import make_response, abort, request
from flask_restful import reqparse, abort, Api, Resource
from flask import make_response, abort, request, redirect, url_for, Flask
from werkzeug.utils import secure_filename
from config import db, basedir
from models.librarymodel import Library
from schemas.libraryschema import LibraryGetSchema, LibraryUpdateSchema
from schemas.librarytemplateschema import LibraryTemplateSchemas
from schemas.templetschema import TemplateSchema



CONFIG_PATH = os.path.join(basedir, 'loggeryaml/librarylogger.yaml')
logging.config.dictConfig(yaml.load(open(CONFIG_PATH), Loader=yaml.FullLoader))
logger = logging.getLogger('getupdatelibrarys')
loggers = logging.getLogger("consolelibrarys")

app = Flask(__name__, static_url_path='/static')
path = os.getcwd()
UPLOAD_FOLDER = path+'/static'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


class GetByIdLibrary(Resource):
    def __init__(self):
        pass

    def get(self, id):
        try:
            library_obj = db.session.query(
                Library).filter(Library.Libaray_Reference == id).first()
            if library_obj:
                library_schema = LibraryTemplateSchemas()
                data = library_schema.dump(library_obj).data
                if data["Control_Step"] == True:
                    data["Control_Step"] = "1"
                else:
                    data["Control_Step"] = "0"
                logger.info("data feteched successfully baesd on id ")
                loggers.info("data feteched successfully baesd on id ")
                return({"success": True, "data": data})
            else:
                logger.warning("Library not found")
                loggers.warning("Library not found")
                return({"success": False, "message": "Library not found"})
        except Exception as e:
            logger.warning(str(e))
            loggers.warning(str(e))
            return({"success": False, "message": str(e)})


class UpdateLibrary(Resource):
    def __init__(self):
        pass

    def put(self, id):
        # try:
            str_data = request.form["data"]
            da = json.loads(str_data)
            print("===================",da)
            if "Template_Title" in da.keys():
                lasttemplates = da["templates"]
                del da["templates"]
            if "Template_Title" in da.keys():
                templateName = da["Template_Title"]
                del da["Template_Title"]
            library_lastrecord = db.session.query(
                Library).order_by(Library.id.desc()).first()
            schema = LibraryUpdateSchema()
            lastrecord = schema.dump(library_lastrecord).data
            created_by = lastrecord["createdby"]
            createdat = lastrecord["created_at"]
            time = str(datetime.datetime.now())
            ref = ''.join([n for n in time if n.isdigit()])
            total_data = ""
            # if library_lastrecord:
            #     lastrecord = schema.dump(library_lastrecord).data
            #     Version_id = lastrecord["Libaray_Reference"]
            #     da.update({"Libaray_Reference": ref, "Version_id": Version_id})
            # else:
            da.update({"Libaray_Reference": ref, "Version_id": id, "createdby": created_by,
                       "updated_at": str(datetime.datetime.utcnow()), "created_at": createdat})
            userId = da["updatedby"]
            if da["Template"] == "0":
                new_library = schema.load(da, session=db.session).data
                db.session.add(new_library)
                db.session.commit()
                data = schema.dump(new_library).data
                total_data = data
                logger.info("library data posted successfully")
                loggers.info("library data posted successfully")
            else:
                files = request.files.getlist("file")
                print("=================",files)
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
                print("--------------------------",data)
                total_data = data
                library_id = data["id"]
                logger.info("library data posted successfully")
                loggers.info("library data posted successfully")
                try:
                    if data != {}:
                        # template_names = json.loads(templateName)
                        for last_templates in lasttemplates:
                            template_dict = {
                                "Template_Title": last_templates["Template_Title"], "Template_File": last_templates["Template_File"], "user_id": userId, "library_id": library_id}
                            template_schema = TemplateSchema()
                            new_template = template_schema.load(
                                template_dict, session=db.session).data
                            db.session.add(new_template)
                            db.session.commit()
                            temp_data = template_schema.dump(
                                new_template).data
                            logger.info(
                                "template data posted successfully")
                            loggers.info(
                                "template data posted successfully")
                        if files != []:
                            url_path = []
                            for name_files in files:
                                filename, file_extension = os.path.splitext(
                                    name_files.filename)
                                time_date = str(datetime.datetime.now())
                                ref2 = ''.join([n for n in time_date if n.isdigit()])
                                fileextension = ref2+file_extension
                                # rename_file = os.rename(name_files.filename, ref)
                                filename = secure_filename(name_files.filename)
                                name_files.save(os.path.join(
                                    app.config['UPLOAD_FOLDER'], filename))
                                os.rename(os.path.join(
                                    app.config['UPLOAD_FOLDER'], filename), os.path.join(app.config['UPLOAD_FOLDER'], fileextension))
                                url_path.append(
                                    url_for("static", filename=fileextension))
                            totaldata = dict(zip(templateName, url_path))
                            for key, value in totaldata.items():
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
                            logger.info("no files are there to create")
                            loggers.info("no files are there to create")
                    else:
                        logger.info("Library not created")
                        loggers.info("Library not created")
                        return({"success": False, "message": "Library not created"})
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
                #     return ({"success": False, "message": "already file exists {}".format(check)})
            logger.info({"success": True, "data": total_data})
            loggers.info({"success": True, "data": total_data})
            return({"success": True, "data": total_data})
        # except Exception as e:
        #     logger.warning(str(e))
        #     loggers.warning(str(e))
        #     return({"success": False, "message": str(e)})

