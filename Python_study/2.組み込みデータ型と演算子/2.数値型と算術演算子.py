#!/usr/bin/env python
# coding: utf-8

# In[1]:


#In[1]

x=100
print(type(x))


# In[2]:


#In[2]

x=100.0
print(type(x))


# In[3]:


#In[3]

#1.25×10**3
x=1.25e3
print(x)


# In[4]:


#In[4]

x=1000.0e-3
print(x)


# In[6]:


#In[5]

x=2+3j
print(type(x))


# In[7]:


#In6

print(15+10)
print(15-10)
print(15*10)
print(15/10)


# In[8]:


x=10**0.5
print(x)


# In[9]:


#In[1]
#切り捨て除算

x=10//3
print(3)


# In[11]:


#In[2]
#負の数を計算する場合注意
#-2.5を超えない最小整数を計算

x=-15//6
print(x)


# In[12]:


#割り算したときの余りを算出
x=10%3
print(x)


# In[1]:


#In[1]
#型の異なる数値同士の計算は広い型に合わせられる
10.0+5


# In[2]:


#In[2]
(1+2j)+3


# In[1]:


#1[1]

class Class_A:
    def__init__(self,obj):
       self.val=obj 


# In[2]:


#In[2]

#Object_Aのインスタンスを生成
x=Class_A(10)
y=Class_A(20)

#aとbを加える
print(x+y)


# In[6]:


#In[3]

class Class_A:
    def __init__(self,obj):
       self.val=obj 
    
    #オブジェクトの加算を定義する
    def __add__(self,other):
        return self.val+other.val


# In[8]:


# In[4]

x = Class_A(10)
y = Class_A(20)

print(x + y)


# In[9]:


#In[5]

class Class_B:
    def __init__(self,obj):
        self.val=obj
        
    # +に掛け算の機能を割り当てる
    def __add__(self,other):
        return self.val * other.val
    
x=Class_B(10)
y=Class_B(20)

print(x+y)


# In[15]:


# In[6]

class Class_C:
    def __init__(self,obj):
        self.val=obj
    
    #オブジェクトの加算を定義する
    def __add__(self,other):
        return"Hello!"
    
x=Class_C(10)
y=Class_C(20)

print(x+y)


# In[16]:


#In[6]

print("りんご"+"みかん")


# In[17]:


#In[8]

class Class_D:
    def __init__(self,obj):
        self.val=obj
        
    #オブジェクトの加算を定義する
    def __add__(self,other):
        return self.val+"と"+other.val
    
x=Class_D("りんご")
y=Class_D("みかん")

print(x+y)


# In[ ]:




