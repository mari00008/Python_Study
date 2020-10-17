#!/usr/bin/env python
# coding: utf-8

# In[5]:


x = (range(10))
print(x)


# In[6]:


x =list((range(10)))
print(x)


# In[7]:


x = list (range(1,10,2))
print(x)


# In[8]:


#降順に
x = list(range(10,0,-1))
print(x)


# In[9]:


#range(5)の要素を全て足す
#すなわち1+2+3+4+5
s = sum(range(5))
print(s)


# In[16]:


#rangeオブジェクトから順に値を取り出す
for x in range (10):
    print(x,end ="")


# In[18]:


#ループ回数をカウント
count = 0
for x in range (100):
    count += 1
print("ループ回数は{}です".format(count))


# In[19]:


for x in range (3):
    print("Pythonは楽しいな")


# In[ ]:




