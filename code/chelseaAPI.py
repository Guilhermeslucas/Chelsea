from flask import Flask, request
from flask_restful import Resource, Api
from socio_economico import execute_socio_analisys, execute_color_analisys

app = Flask(__name__)
api = Api(app)


class DataByColor(Resource):
    def get(self, color):
        return execute_color_analisys(color)


class DataBySalary(Resource):
    def get(self, salary):
        return execute_socio_analisys(salary)


api.add_resource(DataByColor, '/color/<color>')
api.add_resource(DataBySalary, '/salary/<salary>')
if __name__ == '__main__':
    app.run()
