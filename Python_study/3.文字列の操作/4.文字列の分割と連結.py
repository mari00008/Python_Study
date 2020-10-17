#!/usr/bin/env python
# coding: utf-8

# In[4]:


# PYTHON_SPLIT_01
#str.split(区切り文字 [,分割数])

nobel= "まんち/まんぎん/魚肉まん/タートルまんち/ブルーまんぎん"

#"/"で文字列を分割してリスト作成
nobel = nobel.split("/")

print(nobel)


# In[6]:


# PYTHON_SPLIT_02
#str.split(区切り文字 [,分割数])

nobel= "まんち/まんぎん/魚肉まん/タートルまんち/ブルーまんぎん"

#右から2個目の"/"まで区切る
nobel = nobel.split("/",2)

print(nobel)


# In[7]:


#PYTHON_SPLIT_03

nobel_1 = "マルコーニ ファン・デル・ワース ヴィーン ダレーン オネス"
nobel_2 = "  ラウエ   ブラッグ バークラ    プランク   シュタルク   "

#半角スペースをデミタリとして区切る
nobel_1 = nobel_1.split()

#連続した半角スペースは1つのデミタリとして認識
#先頭と末尾の半角スペースは無視される
nobel_2 = nobel_2.split()

print(nobel_1)
print(nobel_2)


# In[9]:


# PYTHON_RSPLIT_01
#str.rsplit(区切り文字 [,分割数])

#ノーベル物理学賞受賞者
nobel ="ギヨーム/アインシュタイン/ボーア/ミリカン/シーグバーン"

#右から3個目の"/"まで区切る
nobel = nobel.rsplit("/",2)

print(nobel)


# In[12]:


# PYTHON_SPLITLINES_01

my_str = "湯川秀樹は原子核内部において陽子と中性子を互いに結合させる中間子の存在を予言しました。\n1947年に英国の物理学者パウエルが宇宙線の中からパイ中間子を発見し、理論の正しさが証明されます。\nこれによって湯川秀樹に日本人初となるノーベル物理学賞が授与されました。"

#文字列を改行位置で区切ってリストを作成する
my_str = my_str.splitlines()

print(my_str)


# In[13]:


# PYTHON_SPLITLINES_02

my_str = "ノーベル物理学賞を英訳すると Nobel Prize in Physics です。\n開催地スウェーデンでは Nobelpriset i fysik と綴ります。\nこのように両言語の発音や表記には類似性があります。\n英語とスウェーデン語はともにゲルマン語派に属する言語です。"

# 文字列を改行位置で区切ってリストを作成します
my_str = my_str.splitlines(True)

print(my_str)


# In[14]:


#PYTHON_RATITION

# ノーベル物理学賞受賞者
nobel = "フランク/ヘルツ/ペラン/コンプトン/ウィルソン"

# 一番左端にある "/" で区切ってタプルを生成します
nobel = nobel.partition("/")

print(nobel)


# In[15]:


# PYTHON_RPARTITION

# ノーベル物理学賞受賞者
nobel = "リチャードソン/ブロイ/ラマン/ハイゼンベルク/シュレーディンガー"

# 一番右端にある "/" で区切ってタプルを生成します 
nobel = nobel.rpartition("/")

print(nobel)


# In[16]:


# PYTHON_JOIN_01

# ノーベル物理学賞受賞者のリスト
nobel = ["ディラック", "チャドウィック", "ヘス", "アンダーソン", "デイヴィソン"]

#リストの各要素を","で結合
nobel = ",".join(nobel)

print(nobel)


# In[17]:


# PYTHON_JOIN_02

# ノーベル物理学賞受賞者のセット
#タプルは順番が崩れるので注意
nobel = {"ディラック", "チャドウィック", "ヘス", "アンダーソン", "デイヴィソン"}

nobel = ",".join(nobel)

print(nobel)


# In[22]:


# PYTHON_JOIN_03

#ノーベル物理学賞(受賞年と受賞者)
nobel = [1937, "トムソン", 1938, "フェルミ", 1939, "ローレンス"]
         
nobel = ",".join(nobel)
         
print(nobel)


# In[23]:


# PYTHON_JOIN_04

#ノーベル物理学賞(受賞年と受賞者)
nobel = [1937, "トムソン", 1938, "フェルミ", 1939, "ローレンス"]
         
#リストのすべての要素を文字列に変換
#str型に統一することでint型が出てきた時のエラーを無くす
nobel = map(str,nobel)

#新しいリストの要素を連結
nobel = ",".join(nobel)
         
print(nobel)

