#!/usr/bin/env python
# coding: utf-8

# In[4]:


# SORT_01-1

#リストを作成
num1 =[4,2,5,1,3]

#昇順に並びかえ
num1.sort()
print(num1)


# In[5]:


num1.sort(reverse = True)
print(num1)


# In[7]:


planets=[(0.33,0.44),(0.55,0.22),(0.22,0.25)]

planets.sort(key = lambda tup : tup [1])

print(planets)


# In[8]:


##itemgetter関数をインポートする
from operator import itemgetter

planets=[(0.33,0.44),(0.55,0.22),(0.22,0.25)]

#キーにリストを並べる
planets.sort(key = itemgetter (1))

print(planets)


# In[9]:


#アルファベットのリストを定義
x = ["D","A","C","E","B"]

#文字を昇順に
x_asc = sorted(x)

x_des =sorted(x, reverse = True)

print(x_asc)
print(x_des)


# In[11]:


x = ["a","A","b","B","c","C"]

x = sorted(x)
print(x)


# In[13]:


#文字列
my_str = "DACEB"

#アルファベットを昇順に並べたリスト
my_str = sorted(my_str)

print(my_str)


# In[14]:


#sorted関数は必ず返しがリスト型になる
#そこで文字列に返してもらうには

#文字列の定義 my_str

#リストの要素を再び結合
my_str = ''.join(my_str)

print(my_str)


# In[16]:


#文字列を昇順、降順に並び替える関数
def str_sort(x,s = False):
    y = sorted(x,reverse = s)
    return ''.join(y)

my_str = "DACBE"

my_str = str_sort(my_str,True)

print(my_str)


# In[20]:


#タプルを定義
num_tup =(1,2,3,4,5,6)

#タプルの要素を降順に並び替えたリストを作成
num_list = sorted(num_tup,reverse = True)

print(num_list)


# In[21]:


#SORTED_06

#ダブルを昇順・降順に並び替える関数
def tup_sort(x,s=False):
    y = sorted(x,reverse = s)
    return tuple(y)

#タプルを定義
num_tup = (1,2,3,4,5,6)

#関数でタプルを後順に
num_tup = tup_sort(num_tup,True)

print(num_tup)


# In[23]:


#リスト定義
framework = ["DJ","Fl","Pl","Bo"]

#並び反転
framework.reverse()

print(framework)


# In[ ]:




