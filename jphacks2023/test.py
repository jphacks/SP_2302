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

#DataFrameの作成
all_df = pd.DataFrame()

#len関数で要素を確認するためのリスト
len_data = []

#料理のデータセット
file_paths = [
                'C:/Users/nanam/Desktop/workspaces/jphacks2023/dataset/_recipes/humbergu.csv',
                'C:/Users/nanam/Desktop/workspaces/jphacks2023/dataset/_recipes/karaage.csv',
                'C:/Users/nanam/Desktop/workspaces/jphacks2023/dataset/_recipes/nikujaga.csv',
                'C:/Users/nanam/Desktop/workspaces/jphacks2023/dataset/_recipes/omuraisu.csv',
                'C:/Users/nanam/Desktop/workspaces/jphacks2023/dataset/_recipes/syogayaki.csv',
            ]

recipi_dataid = ["ハンバーグ","唐揚げ","肉じゃが","オムライス","生姜焼き"]
ingredients_dataid = ['dummy' , 'じゃがいも' , 'リンゴ', 'キャベツ' , 'たまねぎず' , 'たまねぎ' , 'にんじん' , 'マヨネーズ']

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

for vocab_dict in vocab_dict.keys():
  print(vocab_dict)

vectorizer = TfidfVectorizer(tokenizer=tokenize1)
train_matrix = vectorizer.fit_transform(train_X)

print(train_matrix)

# ナイーブベイズを用いて分類
clf = MultinomialNB()
clf.fit(train_matrix, train_y)

# ランダムフォレストを用いて分類
clf2 = RandomForestClassifier(n_estimators=100, random_state=0)
clf2.fit(train_matrix, train_y)

# テストデータを変換
test_matrix = vectorizer.transform(test_X)

# 分類結果を表示
print("ナイーブベイズ")
print("訓練データの正解率:", clf.score(train_matrix, train_ｙ))
print("テストデータの正解率:", clf.score(test_matrix, test_ｙ))
print()
print("ランダムフォレスト")
print("訓練データの正解率:", clf2.score(train_matrix, train_ｙ))
print("テストデータの正解率", clf2.score(test_matrix, test_ｙ))


r = []
result = []
count = 0
path = 'C:/Users/nanam/Desktop/workspaces/jphacks2023/runs/detect/predict/labels/image0.txt'

def conversion(id):
    if id == '0':
        r.append(ingredients_dataid[0])
    elif id == '1':
        r.append(ingredients_dataid[1])
    elif id == '2':
        r.append(ingredients_dataid[2])
    elif id == '3':
        r.append(ingredients_dataid[3])
    elif id == '4':
        r.append(ingredients_dataid[4])
    elif id == '5':
        r.append(ingredients_dataid[5])
    elif id == '6':
        r.append(ingredients_dataid[6])
    elif id == '7':
        r.append(ingredients_dataid[7])


f = open(path)

areas = f.read().split()

for i in areas:
    if count%5 == 0:
        conversion(i)
    count += 1

frzeringr = ' '.join(r)

with open('C:/Users/nanam/Desktop/workspaces/jphacks2023/runs/result/infreezer.csv', 'w', encoding='UTF-8') as f:
    writer = csv.writer(f)
    writer.writerow(['ingredients'])
    writer.writerow([frzeringr])


#-------------------------------------推論（ナイーブベイズ）
sosaku_df = pd.DataFrame()

len_data = []

file = open('C:/Users/nanam/Desktop/workspaces/jphacks2023/runs/detect/predict/labels/image0.txt', 'r', encoding='UTF-8')

file_paths2 = ['C:/Users/nanam/Desktop/workspaces/jphacks2023/runs/result/infreezer.csv']

for file_path in file_paths2:
  sosaku_df = pd.read_csv(file_path, encoding='utf-8')
  sosaku_df = sosaku_df.dropna()
  len_data.append(len(sosaku_df))
  sosaku = sosaku_df['ingredients']

t=Tokenizer()

def tokenize1(text):
    tokens = t.tokenize(text)
    noun = []
    for token in tokens:
      if token.part_of_speech.split(",")[0]=="名詞" and len(token.surface)>1:

        noun.append(token.surface)            
    return noun 

clf = MultinomialNB()
clf.fit(train_matrix, train_y)

# データを変換
sosaku_matrix = vectorizer.transform(sosaku)


print()
# 分類予測結果を表示
print("ナイーブベイズ")
print("作れる料理:", clf.predict(sosaku_matrix))
print()

with open('C:/Users/nanam/Desktop/workspaces/jphacks2023/runs/result/result.csv', 'w') as f:
  if clf.predict(sosaku_matrix) == 0:
      writer = csv.writer(f)
      writer.writerow(['ハンバーグ'])
  elif clf.predict(sosaku_matrix) == 1:
      writer = csv.writer(f)
      writer.writerow(['唐揚げ'])
  elif clf.predict(sosaku_matrix) == 2:
      writer = csv.writer(f)
      writer.writerow(['肉じゃが'])
  elif clf.predict(sosaku_matrix) == 3:
      writer = csv.writer(f)
      writer.writerow(['オムライス'])
  elif clf.predict(sosaku_matrix) == 4:
      writer = csv.writer(f)
      writer.writerow(['生姜焼き'])