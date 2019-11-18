import os
from flask_restful import Api
from config import app
from flask_cors import CORS


api =Api(app)

api = Api(app)
CORS(app)


app.config.from_object(os.environ['APP_SETTINGS'])
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'



from controllers.roles.getpostrole import Getcreateroles
from controllers.roles.getupdatedeleterole import GetUpdateDeleteRoles

api.add_resource(Getcreateroles, '/api/getcreateroles')
api.add_resource(GetUpdateDeleteRoles, '/api/getupdatedeleteroles/<int:id>')


from controllers.users.user_signup import Signup
from controllers.users.user_signin import Signin
from controllers.users.getupdatedeleteuser import GetUpdateUser
from controllers.users.getallusers import Getallusers

api.add_resource(Signup, '/api/signup')
api.add_resource(Signin,'/api/login')
api.add_resource(Getallusers, '/api/getallusers')
api.add_resource(GetUpdateUser, '/api/getupdatedeleteuser/<int:id>')

from controllers.library.getcreatelibrary import GetcreateLibrary
from controllers.library.getbyidupdatedeletelibrary import GetByIdLibrary, UpdateLibrary

api.add_resource(GetcreateLibrary, '/api/getcreatelibrary')
api.add_resource(GetByIdLibrary, '/api/getbyidlibrary/<string:id>')
api.add_resource(UpdateLibrary, '/api/getupdatelibrary/<string:id>')



if __name__=='__main__':
    app.run(host='0.0.0.0',port =5001,debug=True)
