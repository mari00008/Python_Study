#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PYTHON_FROAT_01

#不動小数点数の定義
x=0.4

#整数をfloatで定義
y=1.0

#10×(10の３乗)
z=10e3

#xのクラスを調べる
print(type(x),type(y),type(z))


# In[2]:


#PYTHON_FLOAT_02

x=1/10

print(x)


# In[3]:


# #PYTHON_FLOAT_03
#int型をfloat型数値に変更

x=float(100)

print(x)


# In[4]:


#PYTHON_FLOAT_04
#浮動小数点は限りなく近しい数値を出すことはできるが、完全に正確ではない
x=0.0

for ct in range(10):
    x +=0.1
    
print(x)

