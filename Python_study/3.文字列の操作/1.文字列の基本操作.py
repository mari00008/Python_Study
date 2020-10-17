#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PYTHON_STR_01

my_str = "Pythonは楽しい"
print(type(my_str))


# In[2]:


#PYTHON_STR_02

#文字列の定義
my_str = "Python"

#インデックス3の値を取り出す
x = my_str[3]

print(x)


# In[3]:


#PYTHON_STR_03-1

my_str = "ABCDEFG"

#インデックス0～3を切り出します
#開始インデックス：終了インデックス+1
x = my_str[0:4]

print(x)


# In[4]:


# PYTHON_STR_03-2

my_str = "ABCDEFG"

#インデックス3以降をすべて切り出す
x = my_str[3::]

print(x)


# In[8]:


# PYTHON_STR_03-3

my_str = "ABCDEFG"

#インデックス0　から1文字ずつ飛ばしながら切り出し
x = my_str[::2]

print(x)


# In[10]:


# PYTHON_STR_04-1

mystr1 = "今日は日曜日。"
mystr2 = "どこかに遊びに行きたいな。"
print(mystr1 + mystr2)


# In[11]:


# PYTHON_STR_04-2

mystr = "Pythonは楽しいな♪"
print(mystr*3)


# In[14]:


# PYTHON_STR_05-1

my_str = "サイバーセキュリティ"

#文字列を中央寄せ
#str.center(全体の幅 [, 埋める文字])
str_1 = my_str.center(15,"x")
str_2 = my_str.center(20,"□")

print(str_1)
print(str_2)


# In[15]:


# PYTHON_STR_05-2

my_str = "数理計画法"

#文字列を右寄せ
str_1 = my_str.rjust(12,"△")

print(str_1)


# In[16]:


## PYTHON_STR_05-3

my_str = "画像解析"

#文字列を左寄せ
str_1 = my_str.ljust(12,"〇")

print(str_1)


# In[24]:


# PYTHON_STR_06

#木製の質量
mass_J = 1898e24

#地球の質量
mass_E = 5.972e24

#木星と地球の質量比を計算(kg)
mass_raito_JE = int(mass_J / mass_E)

#質量比を添えて出力
#数値と文字列（単位）を合わせて表示するには　str()関数　を使う
print("木星の質量は地球の"+str(mass_raito_JE)+"倍です")
print(mass_raito_JE)
#print("木星の質量は地球の"+(mass_raito_JE)+"倍です")だとエラーが起こる

