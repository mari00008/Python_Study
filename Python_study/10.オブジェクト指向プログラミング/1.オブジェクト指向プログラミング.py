#!/usr/bin/env python
# coding: utf-8

# In[1]:


#文字列が分からないとき
#type関数を使う


# In[3]:


#IN[1]

#100のクラス
print(type(100))

#"Python"のクラス
print(type("Python"))

#Trueのクラス
print(type(True))


# In[7]:


#IN[2]

#Rectanglesクラスの定義
class Rectangles:
    #def内部に関数が定義
    def __init__(self,a,b):
        self.width = a
        self.length = b
        
    def area(self):
        return self.width * self.length


# In[8]:


#IN[2]
#Rectanglesクラスのインスタンスを生成
rec = Rectangles(10,20)


# In[9]:


print(rec.width)
print(rec.length)


# In[10]:


print(rec.area())


# In[ ]:




