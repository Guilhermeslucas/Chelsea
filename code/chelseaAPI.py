from flask import Flask, request
from flask_restful import Resource, Api
from socio_economico import execute_socio_analisys, execute_color_analisys
from salarios import salario_nome, salario_cargo, salario_instituto
from orcamento import (get_all_relative_expense_last_6_years,
                       get_abs_expense_last_6_years,
                       get_relative_expense_last_6_years)

app = Flask(__name__)
api = Api(app)


class DataByColor(Resource):
    def get(self, color):
        return execute_color_analisys(color.lower())


class DataBySalary(Resource):
    def get(self, salary):
        return execute_socio_analisys(salary.lower())


class SalaryByName(Resource):
    def get(self, name, uni='unicamp'):
        return salario_nome(name.lower(), uni.lower())


class SalaryByTitle(Resource):
    def get(self, title, uni='unicamp'):
        return salario_cargo(title.lower(), uni.lower())


class SalaryByInstitute(Resource):
    def get(self, inst, uni='unicamp'):
        return salario_instituto(inst.lower(), uni.lower())


class AllExpenses(Resource):
    def get(self):
        return get_all_relative_expense_last_6_years()


class ExpensesPerArea(Resource):
    def get(self, area):
        return get_relative_expense_last_6_years(area.lower())


class AbsExpensesPerArea(Resource):
    def get(self, area):
        return get_abs_expense_last_6_years(area.lower())


api.add_resource(DataByColor, '/social/color/<color>')
api.add_resource(DataBySalary, '/social/salary/<salary>')
api.add_resource(SalaryByName, '/salary/nome/<name>/<uni>')
api.add_resource(SalaryByTitle, '/salary/cargo/<title>/<uni>')
api.add_resource(SalaryByInstitute, '/salary/instituto/<inst>/<uni>')
api.add_resource(AllExpenses, '/expenses/todas/<anything>')
api.add_resource(ExpensesPerArea, '/expenses/relativas/<area>')
api.add_resource(AbsExpensesPerArea, '/expenses/absolutas/<area>')


if __name__ == '__main__':
    app.run()
