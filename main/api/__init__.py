from flask import Blueprint
from flask_restful import Api, Resource, url_for
from flask_restful.utils import cors

api_bp = Blueprint('api', __name__)

api = Api(api_bp)

api.decorators = [cors.crossdomain(origin='*', headers=['accept', 'Content-Type','Authorization'])]

from . import routes