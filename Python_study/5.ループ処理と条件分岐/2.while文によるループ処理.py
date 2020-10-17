#!/usr/bin/env python
# coding: utf-8

# In[8]:


#1～10の数字を順番に表示するプログラム
#xをint型で定義(初期値0)
x=0
#xが10未満の間は処理を繰り返す
while x < 10:
    x += 1
    #間隔開けて横並びにxの値を表示
    print(x,"",end = "")


# In[11]:


#7の倍数を表示する

#xをint型で定義（初期値0）
x = 0

#xが100未満の間に処理を繰り返す
while x < 100:
    x += 1
    if x % 7 == 0:
        print(x," ",end ="")


# In[ ]:




