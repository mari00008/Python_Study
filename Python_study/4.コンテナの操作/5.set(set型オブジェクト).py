#!/usr/bin/env python
# coding: utf-8

# In[1]:


#週間天気予報（日曜日～土曜日）
weather = {"晴れ","くもり","晴れ","雨","雨"}

print(weather)


# In[2]:


#30以下の3の倍数
multiple_3 = {3,6,9,12,15,18,21,24,27,30}

#30以下の5の倍数
multiple_5 = {5,10,15,20,25,30}

#30以下の自然数のうち、3または5で割り切れる
multiple_15 = multiple_3 | multiple_5

#要素の個数
n = len(multiple_15)

print(multiple_15)
print("要素の個数:{}".format(n))


# In[3]:


#30以下の15の倍数
multiple_15 = multiple_3 & multiple_5

#要素の個数
n = len(multiple_15)

print(multiple_15)
print("要素の個数:{}".format(n))


# In[4]:


#9以下の自然数の集合
natural_num = {1,2,3,4,5,6,7,8,9}

#9以下の偶数の集合
even_num = {2,4,6,8}

#9以下の奇数の集合
odd_num = natural_num - even_num

#要素の個数
n = len(odd_num)

print(odd_num)
print("要素の個数:{}".format(n))


# In[9]:


#対称差
C =  natural_num ^ even_num

#要素の個数
n = len(C)
print(C)
print("要素の個数:{}".format(n))


# In[11]:


#setA | setB　と同義
#木星の衛星A
J_sat_A ={"メティス", "アドラステア", "イオ", "エウロパ"}

#木星の衛星B
J_sat_B = {"イオ", "エウロパ", "ガニメデ", "カリスト"}

J_sat_A.union(J_sat_B)


# In[13]:


# &と共通
J_sat_A.intersection(J_sat_B)


# In[15]:


# -
#AにあってＢにもある要素を削除
J_sat_A.difference(J_sat_B)


# In[17]:


#どちらか片方にのみ含まれる集合対象差
#setA ^ setB
J_sat_A.symmetric_difference(J_sat_B)


# In[ ]:




