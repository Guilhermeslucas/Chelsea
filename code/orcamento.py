#!/usr/bin/env python3
import pandas as pd
import re


# i = 0
# with open('../DespesaUnicamp2017.csv', 'r', encoding='ISO-8859-1') as f, open('../DespesaUnicamp2017_FINAL.csv', 'w+', encoding='ISO-8859-1') as w:
#     for line in f:
#         print(line)
#         if i > 0:
#             w.write('"'.join(line[106:].split('""'))[:-3]+'\n')
#         i += 1

# regex = re.compile('\"[A-Za-z0-9\-\.\,\s]+\"')
# with open('../DespesaUnicamp2015_FINAL.csv', 'r', encoding='ISO-8859-1') as f, open('../2015_FINAL.csv', 'w+') as w:
#     for line in f:
#         for group in regex.split(line[:-1]):
#             if group is not ',' and group is not '':
#                 data = []
#                 for e in group.split(','):
#                     if e is not '':
#                         data.append('"' + e + '"')
#                 data = ','.join(data)
#         line = line.partition('"')
#         w.write(data + ',' + '"' + line[2][:-2] + '\n')

# headers = 'UO,Unidade Gestora,Fonte de Recursos,Função,Sub Função,Programa,Ação,Funcional Programática,Elemento,Dotação Inicial,Dotação Atual,Empenhado,Liquidado,Pago,Pago Restos'


         #  2011        2012        2013         2014       2015        2016
budget = [2276804928, 2312319824, 2412955247, 2324035947, 2229499377, 2024419045]

def setup():
    file = '../DespesaUnicamp'
    years = ['2011', '2012', '2013', '2014', '2015', '2016']
    health = 0
    education = 0
    for y in years:
        data = pd.read_csv('../data/orcamento/'+str(y)+'_FINAL.csv', dtype=str, header=0)
        for index, row in data.iterrows():
            if 'saude' in row[0].lower():
                health += float(row[3].replace('.', '').replace(',', '.').strip())
            elif 'educacao' in row[0].lower():
                education += float(row[3].replace('.', '').replace(',', '.').strip())
    return health, education
# print("{0:.2f}".format(health))
# print("{0:.2f}".format(education))

def get_all_relative_expense_last_6_years():
    health, education = setup()
    return {'messages': [{'text':'A porcentagem gasta com saúde nos últimos 6 anos foi de ' + '{0:.2f}'.format(100*float(health/sum(budget))) + '%' + ' e a com educação foi de ' + '{0:.2f}'.format(100*float(education/sum(budget))) + '%'}]}

def get_relative_expense_last_6_years(type):
    health, education = setup()
    if type == 'saude':
        return {'messages': [{'text':'Dei uma olhada aqui e vi que a porcentagem das despesas da Unicamp gasta com saúde nos últimos 6 anos foi de '+ '{0:.2f}'.format(100*float(health/sum(budget))) + '%'}]}
    else:
        return {'messages': [{'text':'Dei uma olhada aqui e vi que a porcentagem das despesas da Unicamp gasta com educação nos últimos 6 anos foi de '+ '{0:.2f}'.format(100*float(education/sum(budget))) + '%'}]}

def get_abs_expense_last_6_years(type):
    health, education = setup()
    if type == 'saude':
        return {'messages': [{'text':'Dei uma olhada aqui e vi que as despesas da Unicamp com saúde nos últimos 6 anos foram de R$'+ '{0:.2f}'.format(health)}]}
    else:
        return {'messages': [{'text':'Dei uma olhada aqui e vi que as despesas da Unicamp com educação nos últimos 6 anos foram de R$'+ '{0:.2f}'.format(education)}]}
