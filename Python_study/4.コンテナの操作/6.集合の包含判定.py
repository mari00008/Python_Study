#!/usr/bin/env python
# coding: utf-8

# In[2]:


myset_A = {"ブラジル","パラグアイ","アルゼンチン"}
myset_B = {"アルゼンチン","ブラジル","パラグアイ"}

#等しいか→等しくないか
tf_1 = myset_A == myset_B

tf_2 = myset_A != myset_B

print(tf_1,tf_2)


# In[3]:


# 南米の国々 A
myset_A = {"ブラジル", "パラグアイ", "エクアドル", "ペルー", "アルゼンチン"}

# 南米の国々 B
myset_B = {"ブラジル","アルゼンチン"}

#AはBを含むか
tf_1 = myset_A >= myset_B

#AはBに含まれるか
tf_2 = myset_A <= myset_B

print(tf_1,tf_2)


# In[4]:


# 南米の国々 A
myset_A = {"ブラジル", "パラグアイ", "アルゼンチン"}

# 南米の国々 B
myset_B = {"アルゼンチン", "ブラジル", "パラグアイ"}

# 南米の国々 C
myset_C = {"アルゼンチン", "ボリビア", "パラグアイ", "コロンビア", "ブラジル"}

#真部分集合（一致していないことを条件とした部分集合）
#AはBの部分集合か
tf_1 = myset_A < myset_B
tf_2 = myset_A < myset_C

print(tf_1,tf_2)


# In[7]:


#上位集合か
# ヨーロッパの国々 A
myset_A = {"イタリア", "イギリス", "ドイツ", "フランス", "デンマーク"}

# ヨーロッパの国々 B
myset_B = {"イギリス", "デンマーク", "フランス"}

#集合Ａは集合Ｂを含むか
tf_1 = myset_A.issuperset(myset_B)
#Bは？
tf_2 = myset_B.issuperset(myset_A)

print(tf_1,tf_2)


# In[11]:


#部分集合か
#AはBの部分集合？
tf_1 = myset_A.issubset(myset_B)
#BはAの部分集合？
tf_2 = myset_B.issubset(myset_A)
print(tf_1,tf_2)


# In[13]:


#AとBは互いに素か
# アフリカの国々 A
myset_A = {"コンゴ","ナイジェリア","南アフリカ"}

# アフリカの国々 B
myset_B = {"ガーナ","コートジボワール","ケニア"}

# アフリカの国々 C
myset_C = {"エジプト","エチオピア","南アフリカ"}

#AとBが素か
tf_1 = myset_A.isdisjoint(myset_B)
tf_2 = myset_A.isdisjoint(myset_C)

print(tf_1,tf_2)


# In[ ]:




