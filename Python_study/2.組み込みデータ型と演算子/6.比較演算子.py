#!/usr/bin/env python
# coding: utf-8

# In[1]:


#代入演算子"＝"と比較演算子“==”は別物
#「a = 1」は「aに1を代入する」
#「a == 1」は「aが1に等しいときはTrueを返し、等しくないときはFlaseを返す」

#「1と1は等しい」の真偽
print(1 == 1)


# In[2]:


#「1と2は等しい」の真偽
print(1 == 2)


# In[3]:


#「1と1は等しくない」の真偽
print(1 != 1)


# In[5]:


#「1と2は等しくない」の真偽
print(1 != 2)


# In[7]:


#「10は20以上である」の真偽
print(10 >= 20)


# In[8]:


#「"ドンキーコング"に"コング"が含まれる」の真偽
print("コング"in"ドンキーコング")


# In[9]:


kobato_friend=["牛","鶏","豚"]

#「kobato_friendに"鶏"が含まれるの真偽」
x = "鶏" in kobato_friend
print(x)


# In[11]:


#「10は7より大きく15より小さい」の真偽
print(7 < 10 < 15)


# In[12]:


#「30は10より大きく20より小さい」の真偽
print(10 < 30 < 20)


# In[13]:


#「7と7と7が等しい」の真偽
print(7 == 7 == 7)


# In[14]:


#「"z"は"a"より大きい」の真偽
print("a" < "z")


# In[18]:


#文字列"a"のコードポイントを取得
cp_a = ord("a")

#文字列"z"のコードポイントを取得
cp_z = ord("z")

print("a のコードポイント：{}".format(cp_a))
print("z のコードポイント：{}".format(cp_z))


# In[19]:


#文字列"A"のコードポイントを取得
cp_A = ord("A")

#文字列"Z"のコードポイントを取得
cp_Z = ord ("Z")

print("Aのコードポイント:{}".format(cp_A))
print("Zのコードポイント:{}".format(cp_Z))


# In[21]:


#「"a"は"A"より大きいの真偽」
print("A" < "a")


# In[22]:


#「"abd"は"abc"より大きい」の真偽
print("abc"<"abd")


# In[23]:


#「"ac"は"abc"より大きい」の真偽
print("abc" < "ac")


# In[24]:


#「"abc"は"ab"より大きいの真偽」
print("ab" < "abc")


# In[25]:


bf = ["x","y","w"] < ["x","y","z"]

print(bf)


# In[26]:


bf = ["a","b","c"] < ["a","b"]

print(bf)


# In[28]:


#["a","b"]と["a","b",0]を比較した場合、2番目でチェック
#3番目は異なる型のため判定に無関係

tf=["a","b"] < ["a","c",0]
print(tf)


# In[35]:


#3番目に異なる型の判定が起きるため、無視できない
#型の違いによるエラーが起きる

tf = ["a","b","c"] < ["a","b",0]

print(tf)


# In[40]:


#In[1]

#質量クラスを定義
class Mass:
    def __init__(self,value,unit="kg"):
        self.value = (value,unit)
        
        #単位がbであればkgに換算
        #1kg=0.45359237
        if unit == "b":
            self.value_kg = 0.45359237 * value
        else:
            self.value_kg = value
            
    #比較演算子「＜」を定義
    def __It__(self,other):
        return self.value_kg < other.value_kg
    
    #比較演算子「<=」を定義
    def __le__(self,other):
        return self.value_kg <= other.value_kg


# In[42]:


#In[2]

#kg単位の質量オブジェクトを生成
m1 = Mass(10,"kg")

print(m1.value)


# In[43]:


#In[3]

#ポンド単位の質量オブジェクトを生成
m2 = Mass(20,"b")

print(m2.value)


# In[48]:


# In[4]

# 10キログラムと20ポンドを比較
print(m1 < m2)


# In[ ]:




