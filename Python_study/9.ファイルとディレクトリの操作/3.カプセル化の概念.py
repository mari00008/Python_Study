#!/usr/bin/env python
# coding: utf-8

# In[3]:


class MyDic:
    def __init__(self,*x):
        
        #空白ディクショナリを用意
        self.dic = {}
        
        #渡された引数にキーを割り当ててディクショナリに格納
        for ct in range(len(x)):
            self.dic[ct] = x[ct]
            
#Mydicクラスのインスタンスを生成
my_color = MyDic("red","blue","green")

#ディクショナリ内容を表示
print("変更前の内容:",my_color.dic)

#ディクショナリの内容を変更
my_color.dic[1] ="yellow"

print("変更後の内容:",my_color.dic)


# In[4]:


class MyDic:
    def __init__(self,*x):
        
        #空白のディクショナリ
        self.__dic = {}
        
        #渡されたキーを割り当ててディクショナリに格納
        for ct in range(len(x)):
            self.__dic[ct] = x[ct]
            
    def show(self):
        return self.__dic
    
    # MyDicクラスのインスタンスを生成
my_color = MyDic("red", "blue", "green")

#ディクショナリの内容を変更
my_color.__dic[1] = "yellow"


# In[5]:


# my_color.__dicを表示
my_color.show()


# In[ ]:




