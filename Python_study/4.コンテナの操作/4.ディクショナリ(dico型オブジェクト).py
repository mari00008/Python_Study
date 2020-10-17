#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PYTHON_DICTIONARY_01-1

#英和辞書
my_dic = {"Japanese":"日本語","French":"フランス語","Spanish":"スペイン語"}

print(my_dic["French"])


# In[2]:


print(my_sic["フランス語"])


# In[3]:


print(my_dic)


# In[5]:


#英和辞書
my_dic = {"car":"車","train":"列車","airplane":"飛行機"}

#新しい要素の追加
my_dic["bicycle"] ="自転車"

print(my_dic)


# In[6]:


#英和辞書
my_dic = {"apple":"りんご","banana":"バナナ","strawberry":"イチゴ"}

#キーを指定して要素を削除
del my_dic["strawberry"]

print(my_dic)


# In[8]:


my_dic = {"cucumber":"きゅうり","tomato":"トマト","pumpkin":"カボチャ"}

#"pumpkin"に対応する値を上書きする
my_dic["pumpkin"]="南瓜"

print(my_dic)


# In[14]:


#英和辞書
my_dic = {"cookie":"クッキー","candy":"飴玉","chocolate":"チョコレート"}
x = "candy" in my_dic
y = "cake" in my_dic
z = "cookie" in my_dic

print("candyは辞書に含まれる？ {}".format(x))
print("cakeは辞書に含まれる？ {}".format(y))
print("cookieは辞書に含まれる？ {}".format(z))


# In[16]:


#和英辞書
my_dic = {"市役所":"city hall",
         "消防署":"fire department",
         "警察署":"police station"}

#辞書の内容を全消去
my_dic.clear()

print(my_dic)


# In[28]:


#和英辞書
my_dic = {"エスプレッソ":"Espresso",
         "カプチーノ":"Cappuccino",
         "マキアート":"macchiato"}

#カプチーノ削除
x = my_dic.pop("カプチーノ","ないよ")

print(x)
print(my_dic)


# In[27]:


y = my_dic.pop("モカ","ないよ")

print(y)


# In[29]:


#辞書に含まれるキーの一覧
x = my_dic.keys()

print(x)


# In[30]:


#辞書に含まれる値の一覧
x = my_dic.values()

print(x)


# In[31]:


my_dic = {"シャーペン":"mechanical pencil",
         "消しゴム":"eraser"}

#"消しゴム"に対応する値を取得
x = my_dic.get("消しゴム","存在しません")

print(x)


# In[32]:


y = my_dic.get("鉛筆","存在しません")
print(y)


# In[33]:


x = my_dic.setdefault("シャーペン","存在しません")
print(x)


# In[34]:


#鉛筆のkeyを取得、無ければ追加した上で取得

y = my_dic.setdefault("鉛筆","pencil")

print(y)
print(my_dic)


# In[35]:


my_dic = {"テーブル":"table", "椅子":"chair", "寝台":"bed"}

#キーと値をすべて取得
x = my_dic.items()

print(x)


# In[36]:


elements = {"As":"ヒ素", "Se":"セレン", "Br":"臭素"}

#ディクショナリのアップデート
#重複すつキーは対応する値に上書きされる
elements.update({"As":"Arsenic", "Se":"Selenium", "Br":"Bromine", "Kr":"Krypton"})

#新しいディクショナリの表示
print(elements)


# In[ ]:




