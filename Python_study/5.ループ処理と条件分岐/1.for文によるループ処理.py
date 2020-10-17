#!/usr/bin/env python
# coding: utf-8

# In[3]:


#ROOP_1

#プログラミング言語　リスト
language = ["Python","C++","Java","PHP","Ruby"]

#リストから順に要素を取り出す
for x in language:
    print(x,end = " ")


# In[4]:


#for [繰り返し変数] in [インテラブルオブジェクト]
#インテラブルオブジェクト：反復処理で要素を取り出せるオブジェクトのこと


# In[15]:


my_str = "Python"

#Pythonを1文字ずつ区切る
for x in my_str:
    print(x,"| ",end = "")


# In[19]:


#Pythonを3回表示
for x in range(3):
    print("Python",end = " ")


# In[20]:


#初期値
asum = 0

#0か10を順にasumに加える
#0+1+
for x in range(11):
    asum += x
print(asum)


# In[22]:


asum = 1
for x in range(2,11):
    asum += x
print(asum)


# In[25]:


#初項1,公比5の等比数列　第5項までの和
gsum = 1

for x in range(4):
    gsum += 5 **(x + 1)
    
print(gsum)


# In[30]:


gum = "山田"
for x in range (4):
    gum += "太郎"
print(gum)


# In[32]:


#X大学の科目コードと科目名
subjects = {"B235":"解析力学","B245":"電磁気学","F115":"群論Ⅰ"}

#科目コード(ディクショナリのキー)を取得
for k in subjects:
    print(k)


# In[35]:


#科目名(ディクショナリの値)
for k in subjects:
    print(subjects[k])


# In[36]:


#科目名を取得します
for k in subjects.values():
    print(k)


# In[37]:


#科目コードと科目名
#kはxと同義
#for k in subjects:　　　　サブジェクトの中のk
#print(k,subjects[k])　　　キー　キーの値
for k in subjects:
    print(k,subjects[k])


# In[38]:


#タプルで同じ事
for x in subjects.items():
    print(x)


# In[4]:


#_POP_11
#試験結果のディクショナリ
#x（氏名）、y（点数）
test_score = {"田中次郎":58,"鈴木ゆかり":72,"中村啓介":84}
for x, y in test_score.items():
    if y <= 59:
        print(x,":不可")
        
    elif 60 <= y <= 69:
        print(x,":可")
        
    elif 70 <= y <= 79:
        print(x,":良")
        
    else:
        print(x,":優")


# In[8]:


import itertools

#お菓子のリスト
list_1 = ["ガトーショコラ","アップルパイ","ティラミス"]

#飲み物リスト
list_2 = ["紅茶","コーヒー","ココア"]

#お菓子と飲み物の組み合わせをすべて取得
for j,k in itertools.product(list_1,list_2):
    print((j,k))


# In[9]:


import itertools

#0～2の数字のペアをすべて取得
for j,k in itertools.product(range(3),range(3)):
    print((j,k),end = ", ")


# In[ ]:




