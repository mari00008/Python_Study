#!/usr/bin/env python
# coding: utf-8

# In[1]:


#LIST_01-1

#フルーツのリスト
fruits = ["りんご","みかん","バナナ"]

#fruitsのクラス取得
tp = type(fruits)

#fruitsのクラスを表示
print(tp)


# In[2]:


#LIST_01-2

#fruitsを表示
print(fruits)


# In[3]:


#LIST_01-3

#リストの1番目の要素の取り出し
print(fruits[0])


# In[4]:


#LIST_02

#お菓子のリスト
sweets = ["チョコ","チーズケーキ","アップルパイ"]

#リストの2番目の要素"チーズケーキ"を"抹茶プリン"に置き換える
sweets[1] = "抹茶プリン"

#sweetsを表示
print(sweets)


# In[5]:


#LIST_09

#フルーツのリスト
fruits = ["りんご","みかん","バナナ"]

#お菓子のリスト
sweets = ["チョコレート","チーズケーキ","アップルパイ"]

#リストを連結
fruits_and_sweets = fruits + sweets

#連結されたリストを表示
print(fruits_and_sweets)


# In[6]:


#LIST_04

#Pythonのパッケージのリスト
packages = ["NumPy","SciPy","SymPy"]

#リストの2番目の要素を削除
del packages[1]

#packagesを表示
print(packages)


# In[7]:


#LIST_05-1

#猫の品種リスト
cats = ["マンチカン","メインクーン","アビシニアン","ベンガル","ヒマラヤン"]

#リストの二番目から4番目の要素を抽出
cats_2 = cats[1:4]

#cats_2の表示
print(cats_2)


# In[8]:


#LIST_05-2

#3番目以降の全ての要素を取り出す
cats_3 = cats[2:]

#最初から2つめまで
cats_4 = cats[:2]

#cats_3とcats_4を表示
print(cats_3)
print(cats_4)


# In[10]:


#APPEND

#リストの定義
animals = ["キリン","カバ"]

#リストの末尾に"シマウマ"を追加
animals.append("シマウマ")

#変更されたリストを表示
print(animals)


# In[12]:


animals.append("サイ", "ゾウ")


# In[15]:


#APPEND-2

#リストの末尾にリスト追加
#オブジェクトを追加
animals.append(["サイ","ゾウ"])

#変更されたリストを表示
print(animals)


# In[16]:


#EXTEND-1

#リストを定義
animals = ["ライオン","トラ"]

#リストの末尾に複数要素を追加
#オブジェクトの中身を追加
animals.extend(["ヒョウ","チーター"])

#変更されたリストを表示
print(animals)


# In[17]:


# EXTEND-2

# リストを定義
animals = ["ライオン", "トラ"]

# リストの末尾に複数要素を追加
animals.extend(("ヒョウ", "チーター"))

# 変更されたリストを表示
print(animals)


# In[18]:


#INSERT

#リストを定義
animals = ["コアラ","カンガルー","クスクス"]

#インデックス1に挿入
animals.insert(1,"ウォンバット")

#変更されたリストを表示
print(animals)


# In[23]:


#POP-1

#川端康成の作品リスト
kawabata = ["鶏","かえる","ふわ"]

#リストの末尾削除
print(kawabata.pop())

#変更されたリストを表示
print(kawabata)


# In[24]:


#POP-2

# 川端康成の作品リスト
kawabata = ["雪国", "古都", "伊豆の踊り子", "山の音", "たんぽぽ"]

#3番目（インデックス2）の要素を削除
#print内でも処理される
print(kawabata.pop(2))

#変更されたリストを表示
print(kawabata)


# In[29]:


#REMOVE-1

# 夏目漱石の作品リスト
soseki = ["三四郎", "こころ", "坊ちゃん", "道草", "夢十夜"]

#"道草"を削除
soseki.remove("道草")

#変更されたリストを表示
print(soseki)


# In[30]:


#REMOVE-2


# 夏目漱石の作品リスト
soseki = ["三四郎", "こころ", "坊ちゃん", "道草", "夢十夜"]

#”鶏”を削除
soseki.remove("鶏")


# In[32]:


# CLEAR

# 宮沢賢治の作品リスト
kenji = ["注文の多い料理店", "銀河鉄道の夜", "セロ弾きのゴーシュ"]

#リストの要素を全て削除
kenji.clear()

print(kenji)


# In[34]:


# リストLIST_15

# 英語の試験の点数
etest = [71,22,55,44,66,44]

#リストの合計
x = sum(etest)

print(x)


# In[35]:


# リストLIST_16

print(max(etest))


# In[36]:


x =  min(etest)
print(x)


# In[37]:


x = len(etest)
print(x)


# In[38]:


mean_etest = sum(etest)/len(etest)

print(mean_etest)


# In[ ]:




