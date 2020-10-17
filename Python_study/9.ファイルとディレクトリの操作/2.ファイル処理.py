#!/usr/bin/env python
# coding: utf-8

# In[13]:


# FRW_01-1

# テキストファイルを新規作成して書き込み専用で開く
f = open ("pynote.txt", mode = "w")

# ファイルに書き込み
f.write("Python")

# ファイルを閉じる
f.close()


# In[14]:


# テキストファイルを読み込み専用で開く
f = open("pynote.txt", mode = "r")

# ファイルの内容を表示
print(f.read())

# ファイルを閉じる
f.close()


# In[17]:


#テキストファイルの追記
f = open("pynote.txt", mode = "a")

#ファイルの末尾に登記
f.write("\nAnaconda")

#ファイルを閉じる
f.close()

#読み込み
f = open("pynote.txt", mode = "r")
         
#ファイルの内容を表示
print(f.read())
         
#ファイルを閉じる
f.close()


# In[30]:


#テキストファイル読み書き両用
f = open("pynote.txt", mode = "a+")

#テキストの内容を読み込んで表示
print(f.read())

f.write("\nJupyter Notebook")

#ファイルを閉じる
f.close()

f = open("pynote.txt", mode = "r")

#ファイルの内容を表示
print(f.read())

f.close


# In[25]:


#テキストファイル読み書き両用
f = open("pynote.txt", mode = "a+")

#テキストの内容を読み込んで表示
print(f.read())

f.write("\nJupyter Notebook")

#ファイルを閉じる
f.close()


# In[28]:


#テキストファイルの新規作成と書き込み専用で開く
f = open ("pybook.txt",mode = "w",encoding = "utf-8")

#ファイルに書き込み
f.write("Python 数値計算入門")

#ファイルを閉じる
f.close()


# In[32]:


f = open("pybook.txt", mode = "r",encoding = "utf-8")

print(f.read())

f.close


# In[33]:


with open ("pyfile.txt","w") as f:
    f.write("Matplotlib")
    
with open("pyfile.txt","r") as f:
    print(f.read())


# In[34]:


with open ("pyfile_1.txt", "w",encoding = "utf-8")as f:
    f.write("今日もpython、明日も　python")
    
with open ("pyfile_1.txt","r",encoding = "utf-8")as f:
    my_str = f.read()
    print(my_str)


# In[41]:


with open ("pyfile_2.txt","w",encoding="utf-8") as f:
    f.write("AAAAAA\n\B")
    
with open("pyfile_2.txt","r",encoding= "utf-8") as f:
    my_str = f.readline()
    print(my_str)


# In[42]:


with open("pyfile_2.txt", "r", encoding = "utf-8") as f:
    my_str = f.readline(2)
    print(my_str)


# In[49]:


with open ("pyfile_3.txt","w",encoding = "utf-8") as f:
    f.write("カプセル化\nあ\nいうえ")
    
with open ("pyfile_3.txt","r",encoding = "utf-8") as f:
           my_list = f.readlines()
           print(my_list)


# In[ ]:




