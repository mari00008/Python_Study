#!/usr/bin/env python
# coding: utf-8

# In[29]:


#queueモジュールをインポート
import queue

#キュー作成
q = queue.Queue()

#データを用意
date =["red","blue","green"]

#キューにデータを格納
for i in date:
    q.put(i)


# In[30]:


#キューが満杯になっているか確認
print(q.full())


# In[33]:


print(q.qsize())


# In[34]:


#notで否定された条件を満たすまで繰り返し実行
while not q.empty():
    print(q.get())


# In[39]:


#さらに要素を取り出す
print(q.get(block=False))


# In[40]:


#5秒以内に要素を取り出せなければエラー送出
print(q.get(timeout=5))


# In[42]:


#キューが空になっていることを確認
print(q.empty())


# In[43]:


#格納上限数3のきゅー作成
q = queue.Queue(3)

#キューにデータを格納
for i in range(10):
    q.put(i,block=False)


# In[44]:


print(q.full())


# In[45]:


while not q.empty():
    print(q.get())


# In[3]:


import queue

#LIFOキュー（スタック）を作成
s = queue.LifoQueue()

#データを用意
data = ["red","blue","green"]

#キューにデータを格納する
for i in data:
    s.put(i)
    
#空になるまで要素を取り出す
while not s.empty():
    print(s.get())


# In[4]:


import queue

#優位準付きキューにデータを生成
p = queue.PriorityQueue()

#データを用意
numbers = [5,3,7,1,4]

#キューにデータを格納
for i in numbers:
    p.put(i)

#キューが空になるまで要素を取り出す
while not p.empty():
    print(p.get(),end=" ")


# In[5]:


import collections

q = collections.deque()

#デックを0～2の数字を右側から追加
for i in range(3):
    q.append(i)
    
#デックの中身を表示
print(q)


# In[6]:


#デックに左側から文字列"a"を追加
q.appendleft("a")

print(q)


# In[7]:


#インデックス3の位置に"b"を追加
q.insert(3,"b")

print(q)


# In[10]:


# PYTHON_DEQUE-4

# 右側から要素を1つ取り出す
print(q.pop())

print(q)


# In[11]:


print(q.popleft())

print(q)


# In[12]:


#リストを定義
list_1=["a","b","c"]

#リストの要素をキューに格納
q = collections.deque(list_1)

#キューの中身を表示
print(q)


# In[13]:


#リストを定義
list_2 = [0,1]

#キューの右側にリストを付け加える
q.extend(list_2)

print(q)


# In[14]:


list_3 = [2,3]

q.extendleft(list_3)
print(q)


# In[16]:


#キューの要素を右に3つずらす
q.rotate(3)

print(q)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




