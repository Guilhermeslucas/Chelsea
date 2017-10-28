import csv
import pandas as pd

#function used to open the dataset to make some analysis
def open_dataset():
    files = {}

    for year in range(2014,2017):
        ifile = open('../data/socioeconomico/perfil{}.csv'.format(year), 'r')
        reader = csv.reader(ifile)
        files[str(year)] = reader

    return files

#function used to split table
def split_table(files):
    index_by_years = {}
    for key, ufile in files.items():
        index = 0
        list_index = []
        for row in ufile:
            if 'Tabela' in row[0]:
                list_index.append(index)
            index = index + 1

        index_by_years[key] = list_index
    return index_by_years

#slicing the dataset to get all the tables separated
def index_to_pandas(index_by_years):
    tables_by_year = {}
    for year, indexes in index_by_years.items():
        year_file = pd.read_csv('../data/socioeconomico/perfil{}.csv'.format(year), dtype=object)

        i = 0
        tables_by_year[year] = []
        while i < len(index_by_years[year]) - 1:
            tables_by_year[year].append(year_file[index_by_years[year][i]+1:index_by_years['2014'][i+1]-1])
            i = i + 1

    return tables_by_year

#make some analysis on skin color of analised people
def color_stats(tables_by_year):
    color_dict = {'branco': 2, 'negro': 3, 'pardo': 4 }
    print("Em 2014, a porcentagem de brancos foi "+tables_by_year['2014'][3].iloc[2,4])
    print("Em 2015, a porcentagem de brancos foi "+tables_by_year['2015'][3].iloc[2,4])
    print("Em 2016, a porcentagem de brancos foi "+tables_by_year['2016'][3].iloc[2,4])
    print(" ")
    print("Em 2014, a porcentagem de negros foi "+tables_by_year['2014'][3].iloc[3,4])
    print("Em 2015, a porcentagem de negros foi "+tables_by_year['2015'][3].iloc[3,4])
    print("Em 2016, a porcentagem de negros foi "+tables_by_year['2016'][3].iloc[3,4])
    print(" ")
    print("Em 2014, a porcentagem de pardos foi "+tables_by_year['2014'][3].iloc[4,4])
    print("Em 2015, a porcentagem de pardos foi "+tables_by_year['2015'][3].iloc[4,4])
    print("Em 2016, a porcentagem de pardos foi "+tables_by_year['2016'][3].iloc[4,4])

dici = open_dataset()
final = split_table(dici)
color_stats(index_to_pandas(final))
#for key, value in index_to_pandas(final).items():
#    print("AAAAAAAAAAAAAAAAAAAAAAAAAaa")
#    print(value[3].iloc[4,4])
#    print("BBBBBBBBBBBBBBBBBBBBBBBBBBb")
