# coding: utf-8
from goolabs import GoolabsAPI
import pandas as pd
import csv

all_df = pd.DataFrame()
re=""
n= [[]]*100

app_id = "96071dfd92fdcc4c98d0a2bc474bb08321d272fd352df7ca997122363ea9cfb8"
api = GoolabsAPI(app_id)

file_paths = [
                'C:/Users/nanam/Desktop/workspaces/jphacks2023/dataset/recipes/humbergu.csv',
                'C:/Users/nanam/Desktop/workspaces/jphacks2023/dataset/recipes/karaage.csv',
                'C:/Users/nanam/Desktop/workspaces/jphacks2023/dataset/recipes/nikujaga.csv',
                'C:/Users/nanam/Desktop/workspaces/jphacks2023/dataset/recipes/omuraisu.csv',
                'C:/Users/nanam/Desktop/workspaces/jphacks2023/dataset/recipes/syogayaki.csv',
            ]

_file_paths = [
                'C:/Users/nanam/Desktop/workspaces/jphacks2023/dataset/_recipes/humbergu.csv',
                'C:/Users/nanam/Desktop/workspaces/jphacks2023/dataset/_recipes/karaage.csv',
                'C:/Users/nanam/Desktop/workspaces/jphacks2023/dataset/_recipes/nikujaga.csv',
                'C:/Users/nanam/Desktop/workspaces/jphacks2023/dataset/_recipes/omuraisu.csv',
                'C:/Users/nanam/Desktop/workspaces/jphacks2023/dataset/_recipes/syogayaki.csv',
            ]

nowpath = 4

recipe_df0 = pd.read_csv(file_paths[nowpath], encoding='utf-8')
list1 = recipe_df0['ingredients'].to_list()
for ele in list1:
    response = api.morph(sentence=ele)
    res = response['word_list'][0]
    with open(_file_paths[nowpath], 'a', encoding='UTF-8') as f:
        writer = csv.writer(f)
        for i in res:
            if i[1] == '名詞':
                re += " "+i[2]
        writer.writerow([re])
        re = ""
