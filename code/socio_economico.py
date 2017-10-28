import csv

def open_dataset():
    files = {}

    for year in range(2013,2018):
        ifile = open('../data/socioeconomico/perfil{}.csv'.format(year), 'r')
        reader = csv.reader(ifile)
        files[str(year)] = reader

    return files

dici = open_dataset()
for row in dici['2013']:
    print(row)
