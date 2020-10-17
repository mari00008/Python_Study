#!/usr/bin/env python
# coding: utf-8

# In[1]:


file_path = r"C:\Users\****\Desktop\PythonStudy\9.ファイルとディレクトリの操作"


# In[2]:


import os

#作業フォルダ取得
folder_name = os.getcwd()

print(folder_name)


# In[3]:


from os import path

#作業フォルダの下に"mybook"を連結したパスを生成
p = path.abspath("mybook")

print(p)


# In[4]:


from os import path

#使用中のOSに合わせてパスを組み立てる
p = path.join("C:","Users","****","Desktop","PythonStudy","9.ファイルとディレクトリの操作")
print(p)


# In[5]:


name_list = ["C:","Users","****","Desktop","PythonStudy","9.ファイルとディレクトリの操作"]

p = path.join(*name_list)

print(p)


# In[ ]:





# In[ ]:




