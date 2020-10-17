#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PYTHON_FORMAT_01

#名前の差し込み処理
subject = "{}は2年次の必須項目です".format("情報代数学")

print(subject)


# In[8]:


#PYTHON_FORMAT_02

subject = "{}は2年次の必須科目です"

#科目リスト
subject_list = ["論理回路","アルゴリズム","プログラミング技法"]

#差し込み処理
for x in subject_list:
    y = subject.format(x)
    print(y)


# In[10]:


#PYTHON_FORMAT_03

#位置因数を指定して差し込む
subject = "{0},{1},{2}".format("情報統計学","計算量理論","データ科学")

print(subject)


# In[35]:


# PYTHON_FORMAT_04

my_str = "{subject}の講義は{name}教授が担当します"

x = "情報解析学"
y = "花塚"

my_str = my_str.format(subject = x, name= y)

print(my_str)


# In[16]:


#PYTHON_FORMAT_05

#科目名と担当教授名のディクショナリ
my_dic = {"subject":"ソフトウェア工学","name":"花塚"}

#差し込み位置にキーを指定
my_str ="{0[subject]}の講義は{0[name]}教授が担当します。"

#ディクショナリを使って差し込み処理を実行
my_str =my_str.format(my_dic)

print(my_str)


# In[27]:


#PYTHON_FORMAT_05

#科目名と担当教授名のディクショナリ
my_dic = {"subject":"ソフトウェア工学","name":"花塚"}

#差し込み位置にキーを指定
my_st ="{0[subject]}の講義は{0[name]}教授が担当します。"

#ディクショナリを使って差し込み処理を実行
my_sts =my_st.format(my_dic)

print(my_sts)


# In[28]:


#PYTHON_FORMAT_06

#3桁ごとにカンマで区切る
x = "{:,}円".format(12000)
y = "{:,}円".format(7852000)

print(x,y)


# In[31]:


#PYTHON_FORMAT_07

#数字をパーセンテージで表示
#"."のあとに小数点以下の桁数を指定
x = "{:.2%}".format(1/3)
y = "{:.3%}".format(1/3)
z = "{:.4%}".format(1/3)

print(x,y,z)


# In[34]:


#PYTHON_FORMAT_08

#11文字の長さをとって左寄せ、残りはa
str_left = "{:a<11}".format("情報倫理学")
str_right = "{:a>11}".format("情報")
str_center = "{:^11}".format("情報")

print(str_left)
print(str_right)
print(str_center)


# In[41]:


# PYTHON_FORMAT_04

x = "情報解析学"
y = "花塚"

my_str =f"{x}の講義は{y}教授が担当します"
print(my_str)


# In[43]:


# PYTHON_FORMAT_10

# 3桁ごとにカンマで区切る
x = f"{4511020:,}円"

print(x)


# In[47]:


# PYTHON_FORMAT_11

num = 1/3

x = f"{num:.2%}"
y = f"{num:.3%}"
z = f"{num:.4%}"

print(x,y,z)

