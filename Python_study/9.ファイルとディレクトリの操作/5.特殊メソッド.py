#!/usr/bin/env python
# coding: utf-8

# In[4]:


#インスタンス生成と同時に"Hello!"を表示するクラス
class Hello:
    def __init__(self):
        print("Hello!")
        
#Helloクラスのインスタンスを生成
my_object = Hello()


# In[8]:


#クラスを定義
class Return_value:
    def __init__(self,value):
        return value
    
#インスタンスを生成
x = Return_value(10)


#__init__の戻り値はnone固定、retuen構文にnone以外を指定するとエラー


# In[28]:


#Squareクラスを定義
#上記を防ぐためにインスタンス変数はinitに記述しておく

class Square:
    def __init__(self,x):
        
        #引数を2乗してオブジェクトの属性値に格納する
        self.value = x ** 2
        
#Squareクラスのインスタンスを生成
my_object = Square(5)

#value属性を表示
print(my_object.value)


# In[29]:


#プロフィール管理クラス
class Profile:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        
    #デストラクタ
    def __del__(self):
        print("インスタンスは破棄されました")


# In[37]:


#Profileクラスのインスタンスを生成
#marikoがselfインスタンスに渡されて、ほかのname,age,sexを埋めている
MAriko = Profile ("刑部真理子",38,"女性")

#インスタンスのname属性を表示
print(MAriko.name)


# In[38]:


del MAriko


# In[40]:


#インスタンスのname属性を表示
print(MAriko.name)


# In[50]:


#Profileクラスのインスタンスを生成
Suzune = Profile("城戸涼音",26,"女性")

#インスタンスのname属性を表示
print(Suzune.name)


# In[51]:


Suzune = 100

