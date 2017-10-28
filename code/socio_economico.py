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

dici = open_dataset()
final = split_table(dici)
print(index_to_pandas(final))
