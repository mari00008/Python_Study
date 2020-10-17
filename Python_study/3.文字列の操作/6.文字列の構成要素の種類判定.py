#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PYTHON_STR_ISALPHA

my_str_1 = "Python"
my_str_2 = "Python3"
my_str_3 = "Pythonで人工知能を開発する"
my_str_4 = "a = b"

#要素がすべてalphabetic（Letter）であるか
w = my_str_1.isalpha()
x = my_str_2.isalpha()
y = my_str_3.isalpha()
z = my_str_4.isalpha()

print(w,x,y,z)


# In[2]:


#PYTHON_STR_ISNUMERIC

my_num_1 = "123"
my_num_2 = "１２３"
my_num_3 = "ⅠⅡⅢ"
my_num_4 = "一二三"

#要素がすべて数字であるかを判断
w = my_num_1.isnumeric()
x = my_num_2.isnumeric()
y = my_num_3.isnumeric()
z = my_num_4.isnumeric()

print(w,x,y,z)


# In[3]:


#PYTHON_STR_ISALNUM

my_str_1 = "Python"
my_str_2 = "Python3"
my_str_3 = "Pythonで人工知能を開発する"
my_str_4 = "a = 100"

#要素がすべてalphabeticまたは数字であるかを判定
w = my_str_1.isalnum()
x = my_str_2.isalnum()
y = my_str_3.isalnum()
z = my_str_4.isalnum()

print(w,x,y,z)


# In[4]:


#PYTHON_STR_ISDIGIT

my_num_1="123"
my_num_2 = "１２３"
my_num_3 = "ⅠⅡⅢ"
my_num_4 = "一二三"

#半角全角数字であるか
w = my_num_1.isdigit()
x = my_num_2.isdigit()
y = my_num_3.isdigit()
z = my_num_3.isdigit()

print(w,x,y,z)


# In[5]:


#PYTHON_STR_ISUPPER

my_str_1="DATAFRAME"
my_str_2="DataFrame"
my_str_3 = "DATAFRAMEの作成"
my_str_4 = "データフレーム"

#要素がすべて大文字であるか判定
w = my_str_1.isupper()
x = my_str_2.isupper()
y = my_str_3.isupper()
z = my_str_4.isupper()

print(w,x,y,z)


# In[6]:


#PYTHON_STR_ISLOWER

my_str_1 ="Anaconda"
my_str_2 = "anaconda"
my_str_3 = "minicondaというのもあります"
my_str_4 = "アナコンダ"

#要素がすべて小文字か
w = my_str_1.islower()
x = my_str_2.islower()
y = my_str_3.islower()
z = my_str_4.islower()

print(w, x, y, z)


# In[7]:


# PYTHON_STR_ISTITLE

my_str_1 = "Data Analysis With Pandas"
my_str_2 = "Data Analysis with Pandas"
my_str_3 = "Data Analysis With Pandas (Pandasによるデータ分析)"
my_str_4 = "A = B = 100"

#要素がタイトルケースになっているか
w = my_str_1.istitle()
x = my_str_2.istitle()
y = my_str_3.istitle()
z = my_str_3.istitle()

print(w,x,y,z)


# In[11]:


#PYTHON_STR_ISSPACE

#データなし
my_str_1 = ""

#半角スペース
my_str_2 = "   "

# 全角スペース×1
my_str_3 = "　"

#要素が全てスペースか
x = my_str_1.isspace()
y = my_str_2.isspace()
z = my_str_3.isspace()

print(x, y, z)


# In[ ]:




