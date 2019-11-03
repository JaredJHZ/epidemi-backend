from . import api
from ..controller.user_controller import UserController, UserControllerParameter, UserPagination
from ..controller.pacients_controller import PacientController, PacientParameterController, PacientsPagination, AllPacientsController
from ..controller.login_controller import LoginController
from ..controller.disease_controller import DiseaseController, DiseasesParameterController, DiseasesPaginationController, AllDiseasesController

# HERE ARE MY ROUTES

# User routes
api.add_resource(UserController, '/users')
api.add_resource(UserControllerParameter, '/users/<id>')
api.add_resource(UserPagination, '/users/pagination/<pag>')

# login routes
api.add_resource(LoginController, '/login')


# Pacients routes

api.add_resource(PacientController, '/pacients')
api.add_resource(PacientParameterController, '/pacients/<id>')
api.add_resource(PacientsPagination, '/pacients/pagination/<pag>')
api.add_resource(AllPacientsController, '/pacients/all')

# Diseases routes

api.add_resource(DiseaseController, '/diseases')
api.add_resource(DiseasesParameterController, '/diseases/<id>')
api.add_resource(DiseasesPaginationController, '/diseases/pagination/<pag>')
api.add_resource(AllDiseasesController, '/diseases/all')
