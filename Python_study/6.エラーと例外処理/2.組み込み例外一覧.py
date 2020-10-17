#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = ["a","b","c","d"]
#オブジェクトのサイズを取得
print(len(x))


# In[4]:


x = [["a","b"],["d","e",["f","g"]]]
#[["a","b"]と["d","e",["f","g"]]
len(x)


# In[5]:


#文字列を定義
x = "Python"

#文字数をカウント
print(len(x))


# In[6]:


import numpy as np

#arr = [1,2,3,4,5,6,7,8,9]
arr = np.arange(1,10)
#配列の要素数を数える
print(len(arr))


# In[7]:


arr = np.arange(1,10).reshape(3,3)

print(arr)


# In[13]:


arr = np.arange(1,10).reshape(9,1)

print(arr)


# In[14]:


class Object_A:
    def __len__(self):
        return 10
    
x = Object_A()

len(x)


# In[ ]:




