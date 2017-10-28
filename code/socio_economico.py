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
    year_file = pd.read_csv('../data/socioeconomico/perfil2014.csv')
    print(year_file[index_by_years['2014'][0]:index_by_years['2014'][1]+1])

dici = open_dataset()
final = split_table(dici)
index_to_pandas(final)
