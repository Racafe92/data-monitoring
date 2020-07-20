from flask_restx import Namespace, Resource
api = Namespace('Data Monitoring',
                description='Insert and fetch data from monitoring reports csv files')


@api.route('/', endpoint='data-monitoring')
class DataMonitoring(Resource):
    def get(self):
        return "API ok"
