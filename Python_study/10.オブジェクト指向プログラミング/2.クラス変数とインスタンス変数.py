#!/usr/bin/env python
# coding: utf-8

# In[1]:


#In[1]
class My_class:
    x=100


# In[2]:


#In[2]

#My_classのクラス変数xを参照
print(My_class.x)


# In[3]:


#In[3]

#クラス変数を上書きする
My_class.x = 200

#Mt_classのクラス変数xを参照
print(My_class.x)


# In[4]:


#In[4]

#My_classのインスタンスを作成
My_object = My_class()

#クラス変数を参照
print(My_object.x)


# In[5]:


#In[1]

class Class_A:
    def __init__(self,value):
        self.x = value


# In[6]:


#In[2]

object_1 = Class_A(100)

#インスタンス変数を参照
print(object_1.x)


# In[7]:


#In[3]

object_2 = Class_A("apple")

#インスタンス変数を参照
print(object_2.x)


# In[8]:


#In[4]

#インスタンス変数を上書きする
object_2.x = "orange"

#インスタンス変数を参照
print(object_2.x)


# In[9]:


#In[5]

#インスタンス変数yを追加
object_2.y = "banana"

#インスタンス変数yを参照
print(object_2.y)


# In[10]:


#In[1]

#円のクラスを定義
class Circles:
    #円周率の近似値をクラス変数として定義
    pi = 3.141592653589793
    
    #半径、面積、周長をインスタンス変数として定義
    def __init__(self,r):
        self.radius = r
        self.area = self.pi * self.radius** 2
        self.perimeter = 2 * self.pi * self.radius


# In[12]:


#In[2]

#Circlesクラスのインスタンスを生成
c1 = Circles(5)

#クラス変数を参照
print("円周率: {:.5f}".format(c1.pi))

#インスタンス変数を参照
print("半径:{:.3f}".format(c1.radius))
print("面積:{:.3f}".format(c1.area))
print("周長:{:.3f}".format(c1.perimeter))


# In[13]:


#In[1]

class My_class:
    x = 100
    
    my_object = My_class()
    my_object.x = 200
    print(my_object.x)


# In[14]:


#In[2]

#クラス変数を参照
print(My_class.x)

