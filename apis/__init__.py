from flask_restx import Api
from .datamonitoring import api as nsdatamonitoring

api = Api(version='0.1', title='Data Monitoring API',
          description='An API to show monitoring reports values and my skill with Python and REST')

api_version = 1
api_route = '/api/v'+str(api_version)
api.add_namespace(nsdatamonitoring, api_route + '/data-monitoring')
