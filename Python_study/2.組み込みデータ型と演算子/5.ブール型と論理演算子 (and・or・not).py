#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PYTHON_BOOL_01

#TrueとFalseのクラスを調べる
x=type(True)
y=type(False)
print(x,y)


# In[3]:


#PYTHON_BOOL_02

#等式100 ＝＝ 100の真偽値
tf1 = (100 == 100)

#不等式200<100の真偽値
tf2 = (200 < 100)

print(tf1, tf2)


# In[4]:


#PYTHON_BOOL_03

#等式"abc"=="abc"の真偽値
tf1 = ("abc" == "abc")

#等式"abc"=="ABC"の真偽値
tf2 = ("abc" == "ABC")

print(tf1,tf2)


# In[5]:


#PYTHON_BOOL_04

#文字列Pythonの真偽値
x = bool("Python")

#空の文字列の真偽値
y = bool("")

print(x,y)


# In[6]:


#PYTHON_BOOL_05

#要素をもつリストの真偽値
x = bool(("Python","Anaconda"))

#要素をもたないリストの真偽値
y = bool(())

print(x,y)


# In[9]:


#PYTHON_BOOL_06

#ブール型の数値を確認
a = True + 0
b = False + 0

print(a)
print(b)


# In[11]:


# PYTHON_BOOL_06

# ブール型の数値を確認
a = True
b = False

print(a)
print(b)


# In[12]:


#PYTHON_AND_01
#x and y は x かつ y
#xとyがともにTureのときのみTrue
logical_1 = True and True
logical_2 = True and False
logical_3 = False and True
logical_4 = False and False

print(logical_1)
print(logical_2)
print(logical_3)
print(logical_4)


# In[13]:


#PYTHON_AND_02

#複数の条件式が同時に成り立っているかを判定
logical_1 = (10 == 10 and 20 == 20)
logical_2 = (10 == 10 and 20 == 30)
logical_3 = (10 < 20 and 20 < 40)
logical_4 = (10 == 10 and 20 == 20 and 30 == 30)

print(logical_1)
print(logical_2)
print(logical_3)
print(logical_4)


# In[14]:


#一方でもTrueならTrue
logical_1 = True or True
logical_2 = True or False
logical_3 = False or True
logical_4 = False or False

print(logical_1)
print(logical_2)
print(logical_3)
print(logical_4)


# In[16]:


#PYTHON_OR

#複数の条件式のうち、
#少なくとも１つが成り立っているかどうかを判定
logical_1 = (10 == 10 or 20 == 30)
logical_2 = (10 > 20 and 20 > 30)

print(logical_1)
print(logical_2)


# In[17]:


#PYTHON_NOT_01

#真偽値を反転
logical_1 = not True
logical_2 = not False

print(logical_1,logical_2)


# In[18]:


#PYTHON_NOT_02

#真偽値を反転
logical_1 = not (10 == 10)
logical_2 = not (10 == 20)

print(logical_1,logical_2)


# In[ ]:




