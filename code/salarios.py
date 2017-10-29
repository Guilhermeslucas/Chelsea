# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import re
import seaborn as sns


dataset = pd.read_csv('../data/salarios/setembro-2017-6.csv',header=None, error_bad_lines=False,sep=';', names=['Matricula','Nome','Referencia','Bruto','Indenizacoes','Redutor','Descontos_Legais','Liquido','Instituto','Cargo','Deletar'])
dataset.drop('Deletar', axis=1, inplace=True)
cargos_nulos = dataset.Cargo.isnull()
dataset.Cargo.loc[cargos_nulos] = dataset.Instituto.loc[cargos_nulos]
dataset.Instituto.loc[cargos_nulos] = dataset.Liquido.loc[cargos_nulos]
dataset.Liquido.loc[cargos_nulos] = dataset.Descontos_Legais.loc[cargos_nulos]
dataset.Descontos_Legais.loc[cargos_nulos] = dataset.Redutor.loc[cargos_nulos]
dataset.Redutor.loc[cargos_nulos] = dataset.Indenizacoes.loc[cargos_nulos]
dataset.Indenizacoes.loc[cargos_nulos] = dataset.Bruto.loc[cargos_nulos]
dataset.Bruto.loc[cargos_nulos] = dataset.Referencia.loc[cargos_nulos]
dataset.Referencia.loc[cargos_nulos] = ''
dataset.Instituto = dataset.Instituto.replace('.* (.*)', value=r'\1', regex=True)
dataset_usp = pd.read_csv('../data/salarios/USP.txt',index_col=False,error_bad_lines=False,sep=';')

def get_nome(lista,nome_dado):
    nomes_dado = nome_dado.lower().split()
    for nome_busca in lista:
        nomes_busca = nome_busca.lower().split()
        if len(nomes_dado) == 1:
            if nomes_dado[0] == nomes_busca[0]:
                yield nome_busca
        else:
            if nomes_dado[0] == nomes_busca[0]:
                sobrenomes = 1
                for i in range(1,len(nomes_dado)):
                    for j in range(1,len(nomes_busca)):
                        if nomes_dado[i] == nomes_busca[j]:
                            sobrenomes+=1
                if sobrenomes == len(nomes_dado):
                    yield nome_busca

def get_cargo(lista,cargo_dado):
    cargos_dado = cargo_dado.lower().split()
    for cargo_busca in lista:
        cargos_busca = cargo_busca.lower().split()
        nomes = 0
        for i in range(0,len(cargos_dado)):
            for j in range(0,len(cargos_busca)):
                if cargos_dado[i] == cargos_busca[j]:
                    nomes+=1
                if nomes == len(cargos_dado):
                    yield cargo_busca

def get_instituto(lista,inst_dado):
    inst_dado = inst_dado.lower()
    for i in range(len(lista)):
        institutos = lista[i].lower().split('/')
        for instituto in institutos:
            if instituto == inst_dado:
                yield i

# devolve os salarios por nome
def salario_nome(nome,uni='unicamp'):
    if(uni == 'unicamp'):
        nomes = pd.DataFrame(list(get_nome(dataset.Nome,nome)),columns=['Nome'])
        lista_nomes = []
        if(nomes.shape[0] == 0):
            return {'messages': [{'text': 'Nome não encontrado'}]}
        for name in nomes.Nome:
            nomes_iguais = dataset.loc[dataset.Nome==name]
            nomes_iguais = nomes_iguais.reset_index()
            nomes_iguais.Bruto = nomes_iguais.Bruto.astype(float)
            nomes_iguais.Liquido = nomes_iguais.Liquido.astype(float)
            for i in range(nomes_iguais.shape[0]):
                string1 = 'Nome: ' + name
                string2 = '\nSalário Bruto: R${:,.2f}'.format(nomes_iguais.Bruto[i])
                string3 = '\nSalário Líquido(pós descontos): R${:,.2f}'.format(nomes_iguais.Liquido[i])
                string4 = '\n-------------------------------------------------\n'
                lista_nomes.append({'text': string1+string2+string3+string4})
        return {'messages': lista_nomes}
    if(uni == 'usp'):
        nomes = pd.DataFrame(list(get_nome(dataset_usp.Nome,nome)),columns=['Nome'])
        lista_nomes = []
        if(nomes.shape[0] == 0):
            return {'messages': [{'text': 'Nome não encontrado'}]}
        for name in nomes.Nome:
            nomes_iguais = dataset_usp.loc[dataset_usp.Nome==name]
            nomes_iguais = nomes_iguais.reset_index()
            nomes_iguais.Bruto = nomes_iguais.Bruto.astype(float)
            nomes_iguais.Liquido = nomes_iguais.Liquido.astype(float)
            for i in range(nomes_iguais.shape[0]):
                string1 = 'Nome: ' + name
                string2 = '\nSalário Bruto: R${:,.2f}'.format(nomes_iguais.Bruto[i])
                string3 = '\nSalário Líquido(pós descontos): R${:,.2f}'.format(nomes_iguais.Liquido[i])
                string4 = '\n-------------------------------------------------\n'
                lista_nomes.append({'text': string1+string2+string3+string4})
        return {'messages': lista_nomes}

#devolve os salarios do cargo(titulo)
def salario_cargo(titulo, uni='unicamp'):
    if(uni=='unicamp'):
        cargos = pd.DataFrame(list(get_cargo(dataset.Cargo.astype(str),titulo)),columns=['Cargo'])
        lista_cargos = []
        if(cargos.shape[0] == 0):
            return {'messages': [{'text': 'Cargo não encontrado'}]}
        cargos.drop_duplicates(inplace=True)
        for cargo in cargos.Cargo:
            string1 = 'Cargo: ' + cargo
            string2 = '\nTotal de funcionários encontrado: {:d}'.format(dataset.loc[dataset.Cargo == cargo].size)
            string3 = '\nSalário Bruto Médio: R${:,.2f}'.format(dataset.Bruto.loc[dataset.Cargo == cargo].astype(float).mean())
            string4 = '\nSalário Líquido Médio(pós descontos): R${:,.2f}'.format(dataset.Liquido.loc[dataset.Cargo == cargo].astype(float).mean())
            string5 = '\n-------------------------------------------------\n'
            lista_cargos.append({'text': string1+string2+string3+string4+string5})
        return {'messages': lista_cargos}

    if(uni=='usp'):
        cargos = pd.DataFrame(list(get_cargo(dataset_usp.Cargo.astype(str),titulo)),columns=['Cargo'])
        lista_cargos = []
        if(cargos.shape[0] == 0):
            return {'messages': [{'text': 'Cargo não encontrado'}]}
        cargos.drop_duplicates(inplace=True)
        for cargo in cargos.Cargo:
            string1 = 'Cargo: ' + cargo
            string2 = '\nTotal de funcionários encontrado: {:d}'.format(dataset_usp.loc[dataset_usp.Cargo == cargo].size)
            string3 = '\nSalário Bruto Médio: R${:,.2f}'.format(dataset_usp.Bruto.loc[dataset_usp.Cargo == cargo].astype(float).mean())
            string4 = '\nSalário Líquido Médio(pós descontos): R${:,.2f}'.format(dataset_usp.Liquido.loc[dataset_usp.Cargo == cargo].astype(float).mean())
            string5 = '\n-------------------------------------------------\n'
            lista_cargos.append({'text': string1+string2+string3+string4+string5})
        return {'messages': lista_cargos}

# devolve os gastos com funcionarios por instituto(titulo)
def salario_instituto(titulo, uni='unicamp'):
    if(uni=='unicamp'):
        insts = list(get_instituto(dataset.Instituto.astype(str), titulo))
        dados = dataset.iloc[insts]
        x = pd.DataFrame(dados.Cargo.value_counts()).index.values.astype(str)
        n=0
        y = list(range(0,x.shape[0]))
        for i in x:
            y[n] = dados.Bruto.loc[dados.Cargo == i].astype(float).mean()
            n+=1
#        sns.barplot(x,y)
#        plt.show()
        string1 = 'Instituto: ' + titulo.upper() + ' - UNICAMP'
        string2 = '\nDinheiro gasto com salários de funcionários: R${:,.2f}'.format(dados.Bruto.astype(float).sum())
        return  {'messages': [{'text':string1+string2}]}
    if(uni=='usp'):
        insts = list(get_instituto(dataset_usp.Instituto.astype(str), titulo))
        dados = dataset_usp.iloc[insts]
        string1 = 'Instituto: ' + titulo.upper() + ' - USP'
        string2 = '\nDinheiro gasto com salários de funcionários: R${:,.2f}'.format(dados.Bruto.astype(float).sum())
        return  {'messages': [{'text':string1+string2}]}
