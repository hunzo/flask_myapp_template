from flask import Blueprint
from flask_restplus import Api

from myapp.views.appmain import main
from myapp.models.APIModel import UsersModels

blueprint = Blueprint('RestPlus', __name__)


# flask_restplus -> Blueprint
api = Api(blueprint)

# register APIs Model
api.models[UsersModels.user.name] = UsersModels.user

# register flask-restplus Namespace
api.add_namespace(main)
