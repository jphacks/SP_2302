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
sosaku_df = pd.DataFrame()

#len関数で要素を確認するためのリスト
len_data = []


filename = "C:/Users/nanam/Desktop/workspaces/jphacks2023/models/recipe_model.sav"
loaded_model = pickle.load(open(filename, 'rb'))

#file_pathsとしてsosakuのfile pathを指定
file_paths = ['C:/Users/nanam/Desktop/workspaces/jphacks2023/runs/result/testnikujaga.csv']

def tokenize1(text):
    tokens = t.tokenize(text)
    noun = []
    for token in tokens:
      if token.part_of_speech.split(",")[0]=="名詞" and len(token.surface)>1:

        noun.append(token.surface)            
    return noun 

#recipe_dfとしてデータを読み込み、欠損値を削除、all_dfとして結合
for file_path in file_paths:
  sosaku_df = pd.read_csv(file_path, encoding='utf-8')
  sosaku_df = sosaku_df.dropna()
  len_data.append(len(sosaku_df))
  sosaku = sosaku_df['ingredients']

#Tokenizerのインスタンスを作成
t=Tokenizer()

vectorizer = TfidfVectorizer(tokenizer=tokenize1)

# データを変換
sosaku_matrix = vectorizer.transform(sosaku)


print()
# 分類予測結果を表示
print("ナイーブベイズ")
print("作れる料理:", loaded_model.predict(sosaku_matrix))