from . import api
from ..controller.user_controller import UserController, UserControllerParameter, UserPagination, SearchUserController
from ..controller.pacients_controller import PacientController, PacientParameterController, PacientsPagination, AllPacientsController, SearchPacientController
from ..controller.login_controller import LoginController
from ..controller.disease_controller import DiseaseController, DiseasesParameterController, DiseasesPaginationController, AllDiseasesController, SearchDiseaseController
from ..controller.case_controller import CaseController, CasesParameterController, CasesPaginationController, AllCasesController, SearchCaseController, SearchCaseNameController
from ..controller.graphic_controller import GraphicController
# HERE ARE MY ROUTES

# User routes
api.add_resource(UserController, '/users')
api.add_resource(UserControllerParameter, '/users/<id>')
api.add_resource(UserPagination, '/users/pagination/<pag>')
api.add_resource(SearchUserController,'/users/search/<pag>')

# login routes
api.add_resource(LoginController, '/login')


# Pacients routes

api.add_resource(PacientController, '/pacients')
api.add_resource(PacientParameterController, '/pacients/<id>')
api.add_resource(PacientsPagination, '/pacients/pagination/<pag>')
api.add_resource(AllPacientsController, '/pacients/all')
api.add_resource(SearchPacientController,'/pacients/search/<pag>')

# Diseases routes

api.add_resource(DiseaseController, '/diseases')
api.add_resource(DiseasesParameterController, '/diseases/<id>')
api.add_resource(DiseasesPaginationController, '/diseases/pagination/<pag>')
api.add_resource(AllDiseasesController, '/diseases/all')
api.add_resource(SearchDiseaseController,'/diseases/search/<pag>')

#  cases

api.add_resource(CaseController, '/cases')
api.add_resource(CasesParameterController, '/cases/<id>')
api.add_resource(CasesPaginationController, '/cases/pagination/<pag>')
api.add_resource(SearchCaseController,'/cases/search/<pag>')
api.add_resource(SearchCaseNameController,'/cases/search/name/<pag>')
# grafico

api.add_resource(GraphicController,'/graphics')