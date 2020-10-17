#!/usr/bin/env python
# coding: utf-8

# In[3]:


#英語クイズ

x = input ("重力を英訳すると？")

if x == "gravity":
    print("正解です")
    
else:
    print("残念。正解はgravityです")


# In[4]:


#if→else
#↓
#if


# In[13]:


#偶奇判定

#numpyモジュールから乱数を生成する関数を呼び出す
from numpy.random import *

#1～10の整数をランダムに生成
x = randint(1,11)

#xの値を表示
print("x =",x)

#xを2で割った余りが0ならｘは偶数
if x % 2 == 0:
    print("xは偶数です")
    
#そうでない場合はxは奇数
else:
    print("xは奇数です")


# In[ ]:


#大気圏と高度の対応プログラム

#ユーザーに高度の入力を促す
x = imput("高度(km)を入力してください:")

#文字列をfloatに変換
x = float(x)

if x < 12:
    print("対流圏 (Troposphere) です")
    
elif 12<= x < 50:
    print("中間圏 (Mesosphere) です")
        
elif 50<= x < 80:
    print("中間圏 (Mesosphere) です")
    
else:
    print("大気圏外 (outer space) です")


# In[ ]:





# In[ ]:




