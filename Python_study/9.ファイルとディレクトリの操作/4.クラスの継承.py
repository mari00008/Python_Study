#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Rectanglesクラスの定義
class Rectangles:
    def __init__(self, a, b):
        self.width = a
        self.length = b
        
    def area(self):
        return self.width * self.length
    
#Rectanglesクラスを継承してRectangles_2クラスを作成
class Rectangles_2(Rectangles):
    
    #新しいメソッドの追加
    def perimeter(self):
        return self.width * 2 + self.length * 2
    
#Rectangles_2クラスのインスタンスを生成
rec = Rectangles_2(5,10)

#スーパークラスRectangleのメソッドを使用
print("面積",rec.area())

#サブクラスRectangle_2で追加されたメソッド
print("周長",rec.perimeter())


# In[4]:


#Rectanglesクラスを継承してRectangles_3クラスを作成
class Rectangles_3(Rectangles):
    #スーパークラスのarea()メソッドを上書き。
    #上書きされたメソッドを実装するメソッドのオーバーライド
    def area(self):
        return "面積は" + str(self.width * self.length)+ "です。"
    
#Rectangles_3のインスタンスを作成
rec = Rectangles_3(5,10)
    
#上書きされたメソッドの使用
print(rec.area())


# In[5]:


#Rectanglesクラスを継承してSquaresクラスを作成
class Squares(Rectangles):
    
    #super()関数でスーパークラスを呼び出し
    #初期化メソッドの引数a,bにxを渡す
    def __init__(self,x):
        super().__init__(x,x)
        
#Squaresクラスのインスタンス作成
sq =Squares(10)

#正方形の面積の計算
print(sq.area())


# In[ ]:




