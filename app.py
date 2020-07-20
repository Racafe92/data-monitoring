from flask import Flask
from flask_restx import Resource, Api
from apis import api

app = Flask(__name__)
api.init_app(app)


@api.route('/helloworld')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


if __name__ == '__main__':
    app.run(debug=True)
