#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PYTHOM_TUPLE_01-1
#(惑星,赤道半径,密度)
mercury = ("水星",2440,5.43)

print(mercury)


# In[2]:


#PYTHON_TUPLE_01-2

#1番目の要素の削除を試みます
del mercury[0]


# In[3]:


#(惑星,赤道半径,密度)
venus = ("金星",6052,5.24)

#赤道半径を取り出す
print(venus[1])


# In[4]:


# (惑星名, 赤道半径[km], 密度[g/cm^3])
mars = ("火星",3397,3.93)

#公転周期と衛星データの追加
mars +=(1.881,2)

print(mars)


# In[7]:


earth = ("地球",6378,5.52)

print("地球" in earth)


# In[8]:


xyz =(10,20,30)

#変数x,y,zにタプルの要素を代入
x,y,z = xyz

#変数x,y,zを表示
print(x,y,z)


# In[9]:


#タプル　惑星名を定義
planets = ("水星","金星","地球","火星","木星","土星","天王星","海王星")

#インデックス1から4まで切り出す
x = planets[1:5]
print(x)


# In[10]:


#インデクス2以降全て切り出す
x = planets[2::]
print(x)


# In[11]:


#インデクス3から1文字飛ばし
x = planets[3::2]
print(x)


# In[15]:


#太陽系外惑星のディクショナリ

eplanets = {("アンドロメダ座υ","b"):"Saffar",            ("アンドロメダ座υ","c"):"Samh",            ("アンドロメダ座υ","d"):"Majriti",            ("さいだん座ν","b"):"Quijote",            ("さいだん座ν","c"):"Dulcinea",            ("さいだん座ν","d"):"Rocinante",            ("さいだん座ν","e"):"Sancho",            ("かに座ν","b"):"Galileo",            ("かに座ν","c"):"Brahe",            ("かに座ν","d"):"Lipperhey",            ("かに座ν","e"):"Janssen",            ("かに座ν","f"):"Harriot"}
x = eplanets [("かに座ν","d")]
print(x)

