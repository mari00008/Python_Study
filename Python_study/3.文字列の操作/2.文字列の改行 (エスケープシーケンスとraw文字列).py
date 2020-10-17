#!/usr/bin/env python
# coding: utf-8

# In[4]:


#PYTHON_ESCAPE_01

#トリプルクォーテーションで改行を含む文字列を定義
sentence_1 = '''[運動の第１法則]
くぱこ'''

#トリプルダブルクォーテーションで改行を含む文字列を定義
sentence_2 = '''[運動の第２法則]
こんにゃく'''

print(sentence_1)
print(sentence_2)


# In[10]:


#PYTHON_ESCAPE_02

#エスケープシーケンスを使って改行
sentence = "[運動の第3法則]\nスポンジボブ"

print(sentence)


# In[13]:


#PYTHON_ESCAPE_03

#シングルクォーテーションを文字列として定義
sentence = "\'ケプラー1122\'"

print(sentence)


# In[ ]:


#PYTHON_RAW

#raw文字列の定義
#記述通りに表示されるのがrawの良さ
my_path = r"C:\Users\光希\Desktop\PythonStudy\3.文字列の操作"

