import pandas as pd
import csv
import numpy as np
import random
from sklearn.model_selection import train_test_split
from janome.tokenizer import Tokenizer
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
import pickle

#DataFrameの作成
all_df = pd.DataFrame()

len_data = []

file_paths = [
                'C:/Users/nanam/Desktop/workspaces/jphacks2023/dataset/recipes/humbergu.csv',
                'C:/Users/nanam/Desktop/workspaces/jphacks2023/dataset/recipes/karaage.csv',
                'C:/Users/nanam/Desktop/workspaces/jphacks2023/dataset/recipes/nikujaga.csv',
                'C:/Users/nanam/Desktop/workspaces/jphacks2023/dataset/recipes/omuraisu.csv',
                'C:/Users/nanam/Desktop/workspaces/jphacks2023/dataset/recipes/syogayaki.csv',
            ]

def tokenize1(text):
    tokens = t.tokenize(text)
    noun = []
    for token in tokens:
      if token.part_of_speech.split(",")[0]=="名詞" and len(token.surface)>1:

        noun.append(token.surface)            
    return noun 

#recipe_dfとしてデータを読み込み、欠損値を削除、all_dfとして結合
for file_path in file_paths:
  recipe_df = pd.read_csv(file_path, encoding='utf-8')
  recipe_df = recipe_df.dropna()
  len_data.append(len(recipe_df))
  all_df = pd.concat([all_df, recipe_df])

#Tokenizerのインスタンスを作成
t=Tokenizer()

#辞書vocab_dictにリストの各要素の出現回数を記録
vocab_dict = defaultdict(int)

y =  np.array([0]*len_data[0] + [1]*len_data[1] + [2]*len_data[2] + [3]*len_data[3] + [4]*len_data[4])

train_X, test_X, train_y, test_y = train_test_split(all_df['ingredients'],y, random_state=0,train_size=0.7)

print(all_df)