#!/usr/bin/env python
# coding: utf-8

# In[6]:


# PYTHON_VARIABLE_01
#円周率の値を変数piに入れる
pi=3.141593

#半数1.25を変数ｒに入れる
r=1.25

#円の面積を計算して変数ｓに入れる
#**は二乗を表す
s=pi*r**2

#面積sを表示
print(s)


# In[8]:


# PYTHON_VARIABLE_02

#NumPyをnpという名前で読み込む
import numpy as np

#半径1.25を変数ｒに入れる
r=1.25

#円の面積を計算して変数ｓに入れる
s=np.pi*r**2

#面積ｓを表示する
print(s)


# In[10]:


# PYTHON_VARIABLE_03

x="おはようございます。"
ｙ="今日は良い天気ですね。"
print(x+y)


# In[11]:


# PYTHON_VARIABLE_04

x = "おはようございます。"
y = "今日は良い天気ですね。"
x = x + y
print(x)


# In[14]:


#KEYWORD-1

import keyword

#予約語（キーワード）の一覧を取得
kw=keyword.kwlist

print(kw)


# In[16]:


# KEYWORD-2

#予約語（キーワード）の数を調べる
print(len(kw))


# In[19]:


# KEYWORD-3

#awaitが予約語リストに含まれているかを確認する
x=keyword.iskeyword("await")

print(x)


# In[20]:


# KEYWORD-4

#blogcatが予約語リストに含まれているかを確認する
x=keyword.iskeyword("blogcat")

print(x)

