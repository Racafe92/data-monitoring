from flask import Flask
from flask_restx import Resource, Api
from setup.setup import app
from apis import api

api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
