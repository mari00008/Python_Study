#!/usr/bin/env python
# coding: utf-8

# In[1]:


# PYTHON_STR_FIND_01

#str.find(検索文字列[,開始インデックス[,終了インデックス]])

#文字列を定義
my_str = "Python"

#"th"を探す
x = my_str.find("th")

print(x)


# In[2]:


#PYTHON_STR_FIND_02

#文字列を定義
my_str = "Jupyter Notebook"

#範囲を指定して"te"を探します
x = my_str.find("te",8,13)

print(x)


# In[3]:


#PYTHON_STR_FIND_03

#文字列を定義
my_str = "Anaconda"

#"z"を探します
x = my_str.find("z")
print(x)


# In[4]:


#str.rfind (検索文字列 [,開始インデックス [,終了インデックス]])
#右端(末尾)から検索ができる


# In[6]:


#PYTHON_STR_REFIND_01

my_str = "Pythonで人工知能を作るんだ。そのためには毎日家にいるときには隙間時間にはPythonをやっておこう。"

x = my_str.rfind("Python")

print(x)


# In[7]:


#str.index (検索文字列 [,開始インデックス [,終了インデックス]])


# In[10]:


#PYTHON_STR_INDEX

my_str = "Pythonではあらゆることが可能になる。そこまで言うのは大げさかもしれないけれど、Python使うといろいろなことができるよね"

#左端から10番目以降から"Python"を検索
x = my_str.index("Python",10)

print(x)


# In[12]:


#str.rindex (検索文字列 [,開始インデックス [,終了インデックス]])
#末尾から順番に


# In[14]:


# PYTHON_STR_RINDEX

my_str="Pythonや、ああ最近Pythonやってるな"

x = my_str.rindex("Python")

print(x)


# In[15]:


#PYTHON_STR_STARTWITH

#指定範囲内の最初の文字列が一致しているかどうか
#str.startswith (検索文字列[, 開始インデックス[, 終了インデックス]])

my_str = "Method is assciated ..."

#最初の文字列がMethodか
x = my_str.startswith("Method")

print(x)


# In[16]:


#PYTHON_STR_ENDWITH

my_str ="Method is ... an object"

#最後の文字列がMethodか
x = my_str.endswith("object")

print(x)


# In[17]:


#PYTHON_STR_REPLACE_01
#str.replace (置換される文字列, 置換する文字列 [, 置換回数])
my_str = "竹内の竹"

#竹を置き換え
my_str = my_str.replace("竹","かき氷")

print(my_str)


# In[18]:


#PYTHON_STR_REPLACE_02

my_str = "AAA AAA AAA"

my_str = my_str.replace("A","B")

print(my_str)


# In[19]:


#PYTHON_STR_REPLACE_03

my_str = "AAA AAA AAA"

my_str = my_str.replace("A","B",4)

print(my_str)


# In[21]:


#PYTHON_STR_STRIP_01

my_str = "AABABAA"
#両端の"A"全て削除
my_str = my_str.strip("A")

print(my_str)


# In[22]:


# PYTHON_STR_STRIP_02

my_str ="   Miniconda   "
my_str = my_str.strip()

print(my_str)


# In[26]:


# PYTHON_STR_LSTRIP

my ="AACCCAAAAA"

my = my.lstrip("A")

print(my)


# In[27]:


# PYTHON_STR_RSTRIP

my = my.rstrip("A")

print(my)

