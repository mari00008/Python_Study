#!/usr/bin/env python
# coding: utf-8

# In[3]:


#モジュールをインポート
import datetime

#datetime.dateクラスのインスタンス作成
#2018年10月15日
x = datetime.date(2018,10,15)

#xのデータを表示
print("日付:",x)

#xのクラスを表示
print("クラス:",type(x))

#インスタンス変数を使って年月日を表示
print(x.year,"年",x.month,"月",x.day,"日")


# In[4]:


#datetimeモジュールをインポート
import datetime

#datetime.timeクラスのインスタンスを作成
#15時42分19秒
x = datetime.time(15,42,19)

#xのもつデータを表示
print("時刻:",x)

#xのクラスを表示
print("クラス:",type(x))

#インスタンス変数を使って時刻表示
print(x.hour,"時",x.minute,"分",x.second,"秒")


# In[8]:


import datetime

#datetimeオブジェクトのnowメソッドでリアルタイムを取得
x = datetime.datetime.now()

#xの持つデータを表示
print("日付と時刻:",x)

#インスタンス変数を使って年月日
print(x.year,"年",x.month,"月",x.day,"日")

#インスタンス変数を使って時刻表示
print(x.hour,"時",x.minute,"分",x.second,"秒")

print(x.timetuple())


# In[9]:


import datetime

x = datetime.date(2018,11,21)
y = datetime.date(2018,11,20)
print(x-y)

print(type(x-y))


# In[10]:


import datetime

x = datetime.date(2018,5,10)

dx = datetime.timedelta(100)

#100日後の日付を表示
print(x + dx)


# In[11]:


#weekdayは0が月曜日、6が日曜日
import datetime

x = datetime.date(2020,3,22)

#曜日番号の取得
print(x.weekday())


# In[12]:


import datetime

dt = datetime.timedelta(1)

x = datetime.date(2020,3,22)

for k in range(7):
    x += dt
    print(x,"曜日番号",x.weekday())


# In[13]:


import datetime

dweek =["月","火","水","木","金","土","日"]

dt = datetime.timedelta(1)

#起点日時
x = datetime.date(2020,3,22)

#日付と曜日の表示
for k in range(7):
    x += dt
    print(x,dweek[x.weekday()])


# In[14]:


import datetime

#datetime.datetimeクラスのインスタンスを作成
#2018/5/8/17/2/9
x = datetime.datetime(2018,5,8,17,2,9)

#西暦4桁、月2桁、日2桁
print("{:%Y/%m/%d}".format(x))

# 西暦を2桁、月を下2桁、日を下2桁で表示
print("{:%y/%m/%d}".format(x))

# 時を24時間表記、分を2桁、秒を2桁で表示
print("{:%H:%M:%S}".format(x))

# 時を12時間表記、分を2桁、秒を2桁で表示
print("{:%I:%M:%S}".format(x))

# AM,PMの表記、時を12時間表記、分を2桁、秒を2桁で表示
print("{:%p%I:%M:%S}".format(x))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




