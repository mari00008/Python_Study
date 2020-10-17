#!/usr/bin/env python
# coding: utf-8

# In[12]:


#構文エラー
print("Python"


# In[9]:


# インデントエラーの実例

x = 0

# xに1を9回足す
for j in range(10):
x = x + 1
print(x)


# In[11]:


# インデントエラーの実例

x = 0

# xに1を9回足す
for j in range(10):
    x = x + 1
print(x)


# In[14]:


#NameError

print(y + 10)


# In[15]:


#TypeError

print("10"+1)


# In[16]:


# PYTHON_TRY_EXCEPT_01

a = input("数値aを入力してください:")
b = input("数値bを入力してください:")
a = float(a)
b = float(b)

print("a/b = {}".format(a/b))
print("プログラムを終了します")


# In[25]:


#02

a = input("数値aを入力してください:")
b = input("数値bを入力してください:")

try:
    a = float(a)
    b = float(b)
    print("a/b = {}".format(a/b))
    
except ZeroDivisionError:
    print("0では除算できません")
    
print("プログラムを終了")


# In[26]:


# PYTHON_TRY_EXCEPT_03

a = input("数値aを入力してください:")
b = input("数値bを入力してください:")

try:
    a = float(a)
    b = float(b)
    print("a/b = {}".format(a/b))

except ZeroDivisionError:
    print("0では除算できません")
    
print("プログラムを終了します")


# In[28]:


# PYTHON_TRY_EXCEPT_03

a = input("数値aを入力してください:")
b = input("数値bを入力してください:")

try:
    a = float(a)
    b = float(b)
    print("a/b = {}".format(a/b))

except (ZeroDivisionError,ValueError):
    print("不適切")
    
print("プログラムを終了します")


# In[32]:


# PYTHON_TRY_EXCEPT_05

a = input("数値aを入力してください:")
b = input("数値bを入力してください:")

try:
    a = float(a)
    b = float(b)
    print("a/b = {}".format(a/b))

except ZeroDivisionError:
    print("0では除算できません")
    
except ValueError:
    print("ボックスには数値を入力してください")
    
    print("プログラム終了")


# In[33]:


#06

a = 10
b = 0

try:
    print("a/b = {}".format(a/b))
    
except Exception as err:
    print("エラーが発生しました！")
    print("エラーの種類:{}".format(err))


# In[34]:


# PYTHON_TRY_EXCEPT_07

a = input("数値aを入力してください:")
b = input("数値bを入力してください:")

try:
    print(a/b)

except ZeroDivisionError:
    print("0では除算できません")

finally:
    print("プログラムを終了します")


# In[35]:


raise NameError("変数が定義されていません")


# In[37]:


#name

print(G)


# In[38]:


a = math.gaga(6)


# In[40]:


# PYTHON_TYPEERROR_01

print("10" + 1)


# In[41]:


# PYTHON_TYPEERROR_01

print("10" + "1")


# In[42]:


#range型に浮動小数点数(float)を渡す
#整数(int)でなければならない
x = 0

for k in range(10.1):
    x += 1
    

print(x)


# In[44]:


#range型に浮動小数点数(float)を渡す
#整数(int)でなければならない
x = 0

for k in range(10):
    x += 2
    

print(x)


# In[45]:


# PYTHON_INDEXERROR

# リストを定義
my_list = ["NumPy", "SciPy", "pandas"]

# 4番目の要素を参照
x = my_list[3]


# In[48]:


# PYTHON_INDEXERROR

# リストを定義
my_list = ["NumPy", "SciPy", "pandas"]

# 3番目の要素を参照
x = my_list[2]

print(x)


# In[49]:


# PYTHON_KEYERROR

# 辞書を定義
my_dic = {"日曜日":"晴れ",
          "月曜日":"雨",
          "火曜日":"曇り"}

# 4番目の要素を参照
x = my_dic["水曜日"]

print(x)


# In[54]:


my_dic ={"日曜日":"晴れ",
        "月曜日":"雨",
        "火曜日":"曇り"}
#3番目
x = my_dic["日曜日"]

print(x)


# In[55]:


#存在しない関数

from numpy import aaa


# In[56]:


#インポート先のモジュールが見つからない

import nunpy


# In[60]:


my_list = ["a", "b", "c"]

my_iter = iter(my_list)

for i in range(4):
    print(next(my_iter))


# In[61]:


# PYTHON_OVERFLOWERROR

import math

# e=2.718...の1000乗を計算
x = math.exp(1000)

print(x)


# In[62]:


import numpy as np

# e=2.718...の1000乗を計算
x = np.exp(1000)

print(x)


# In[63]:


a = int("Py")

print(a)


# In[64]:


a = int("100")

print(a)


# In[65]:


a = int("100.5")

print(a)


# In[66]:


# PYTHON_ATRIBUTEERROR

x = "Python".uper()

print(x)


# In[68]:


# PYTHON_ATRIBUTEERROR

x = "Python".upper()

print(x)


# In[ ]:




