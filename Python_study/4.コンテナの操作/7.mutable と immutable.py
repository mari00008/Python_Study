#!/usr/bin/env python
# coding: utf-8

# In[1]:


#MUTABLE
#リスト
# 芳香族化合物のリスト
aroma = ["トルエン", "フェノール", "アニソール"]

#フェノールをニトロベンゼンに置き換え
aroma[1] = "ニトロベンゼン"

print(aroma)


# In[2]:


#MUTABLE
#タプル
# 芳香族化合物のリスト
aroma = ("トルエン", "フェノール", "アニソール")

#フェノールをニトロベンゼンに置き換え
aroma[1] = "フェノール"

print(aroma)


# In[5]:


#タプルは置き換え不可能
#このような文字列をイミュータブルという
#置き変えてるように見せて、新しい文字列を作って返しているだけ


# In[6]:


#ベンゾフェノンをベンゾニトリルに変える
x = "benzophenone".replace("phenone","nitrile")

print(x)


# In[7]:


x = "benzophenone"
x.replace("phenone","nitrile")

print(x)


# In[9]:


#変数が作り変えられた方の文字列を参照する
x = "benzophenone"
x = x.replace("phenone","nitrile")

print(x)


# In[ ]:


#ミュータブルなオブジェクトが自身を書き換える操作＝破壊的操作
#リスト、ディクショナリ、set

#イミュータブルなオブジェクトで破壊的操作を伴うメソッドはない
#数値、文字列、タプル

