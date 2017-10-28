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
def color_stats(tables_by_year, color=None):
    if color == 'branco':
        string_2014 = "Em 2014, a porcentagem de brancos foi "+tables_by_year['2014'][3].iloc[2,4]+"."
        string_2015 = " Em 2015, a porcentagem de brancos foi "+tables_by_year['2015'][3].iloc[2,4]+"."
        string_2016 = " Em 2016, a porcentagem de brancos foi "+tables_by_year['2016'][3].iloc[2,4]+"."
        return string_2014+string_2015+string_2016
    elif color == 'negro':
        string_2014 = "Em 2014, a porcentagem de negros foi "+tables_by_year['2014'][3].iloc[3,4]+"."
        string_2015 = " Em 2015, a porcentagem de negros foi "+tables_by_year['2015'][3].iloc[3,4]+"."
        string_2016 = " Em 2016, a porcentagem de negros foi "+tables_by_year['2016'][3].iloc[3,4]+"."
        return string_2014+string_2015+string_2016
    elif color == 'pardo':
        string_2014 = "Em 2014, a porcentagem de pardos foi "+tables_by_year['2014'][3].iloc[4,4]+"."
        string_2015 = " Em 2015, a porcentagem de pardos foi "+tables_by_year['2015'][3].iloc[4,4]+"."
        string_2016 = " Em 2016, a porcentagem de pardos foi "+tables_by_year['2016'][3].iloc[4,4]+"."
        return string_2014+string_2015+string_2016

#make some analysis on economy issues
def economical_stats(tables_by_year, salaries):
    times = [1,2,3,5,7,10,15,20,21]
    if salaries == 1:
        string_2014 = tables_by_year['2014'][9].iloc[2,3]
        string_2015 = tables_by_year['2015'][9].iloc[2,3]
        string_2016 = tables_by_year['2016'][9].iloc[2,3]
    elif salaries == 2:
        string_2014 = tables_by_year['2014'][9].iloc[3,3]
        string_2015 = tables_by_year['2015'][9].iloc[3,3]
        string_2016 = tables_by_year['2016'][9].iloc[3,3]
    elif salaries == 3:
        string_2014 = tables_by_year['2014'][9].iloc[4,3]
        string_2015 = tables_by_year['2015'][9].iloc[4,3]
        string_2016 = tables_by_year['2016'][9].iloc[4,3]
    elif salaries == 5:
        string_2014 = tables_by_year['2014'][9].iloc[5,3]
        string_2015 = tables_by_year['2015'][9].iloc[5,3]
        string_2016 = tables_by_year['2016'][9].iloc[5,3]
    elif salaries == 7:
        string_2014 = tables_by_year['2014'][9].iloc[6,3]
        string_2015 = tables_by_year['2015'][9].iloc[6,3]
        string_2016 = tables_by_year['2016'][9].iloc[6,3]
    elif salaries == 10:
        string_2014 = tables_by_year['2014'][9].iloc[7,3]
        string_2015 = tables_by_year['2015'][9].iloc[7,3]
        string_2016 = tables_by_year['2016'][9].iloc[7,3]
    elif salaries == 15:
        string_2014 = tables_by_year['2014'][9].iloc[8,3]
        string_2015 = tables_by_year['2015'][9].iloc[8,3]
        string_2016 = tables_by_year['2016'][9].iloc[8,3]
    elif salaries == 20:
        string_2014 = tables_by_year['2014'][9].iloc[9,3]
        string_2015 = tables_by_year['2015'][9].iloc[9,3]
        string_2016 = tables_by_year['2016'][9].iloc[9,3]
    else:
        string_2014 = tables_by_year['2014'][9].iloc[10,3]
        string_2015 = tables_by_year['2014'][9].iloc[10,3]
        string_2016 = tables_by_year['2014'][9].iloc[10,3]

    return 'A porcentagem de pessoas com renda de '+str(salaries)+' salarios foi: 2014: '+string_2014+' 2015: '+string_2015+' 2016: '+string_2016

dici = open_dataset()
final = split_table(dici)
index_tables = index_to_pandas(final)
economical_stats(index_to_pandas(final), 2)
#print(color_stats(index_to_pandas(final),'pardo'))
print(economical_stats(index_tables,2))
