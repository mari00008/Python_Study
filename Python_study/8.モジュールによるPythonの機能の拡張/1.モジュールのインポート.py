#!/usr/bin/env python
# coding: utf-8

# In[1]:


#モジュールをインポート
import math

#平方根を計算する関数を引き出して計算
x = math.sqrt(100)

print(x)


# In[2]:


#モジュールから特定の関数だけをインポート
from math import sqrt

#100の平方根を計算
x = sqrt(100)

print(x)


# In[3]:


#複数読み込む
from math import e,pi

print(e,pi)


# In[4]:


#全てのモジュールをインポート

#mathモジュールからすべてのオブジェクト
from math import*

print(e,pi,log(e))


# In[6]:


#randomモジュールをrdという名前でインポート
import random as rd

#乱数生成
x = rd.randint(1,100)

print(x)


# In[7]:


from datetime import datetime as dt
x = dt.now()

print(x)


# In[ ]:




