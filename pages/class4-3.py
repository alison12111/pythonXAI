#  算術指定運算子
a = 1
a += 1  # a=a+1
print(a)  # 2
a -= 1  # a=a-1
print(a)  # 1
a *= 2  # a=a*2
print(a)  # 2
a /= 2  # a=a/2
print(a)  # 1.0
a //= 2  # a=a//2
print(a)  # 0
a %= 2  # a=a%2
print(a)  # 0.0
a **= 2  # a=a**2
print(a)  # 1.0

# 優先順序
# 1.( ) 括號
# 2.** 次方
# 3.*/ // %  乘、除、整除、餘數
# 4.+ - 加減
# 5.< > <= >= == !=比較運算子
# 6.not
# 7.and
# 8.or
# 9.+= -= *= /= //= %= **== 算術指定運算子

#while迴圈
#while會搭背一個條件是來使用
#條件式成為True時會執行迴圈
#條件式成為False時會跳出迴圈
#每次回圈執行完都會重新檢查條件有沒有變成False
1=0
while i<5:
    print(i)
    i+=1  # i=i+1

#break可以強制跳出迴圈
#先判斷break屬於哪個迴圈,然後跳出該迴圈
i=0
while i<5:
    print(i)
    for j in range(5):
        print(j)
        if j==3:
            break #跳出迴圈,屬於while迴圈
        i+=1

for i in range(5):
    print(i)
    if i==3:
        break #跳出迴圈

import random  #匯入random模組

# random.randint()設定抽籤範圍的方式一定要設定開始與結束
#且結束的數字會包含在內
print(random.randint(1,6)) #1-6

ans=random.randint(1,100) #隨機產生1到100的整數
while True: #無窮迴圈
    num=int(input("請輸入1到100的整數:"))  #輸入整數
    if num<0 or num>100: #如果輸入超出範圍
        print("請輸入1到100的整數")
    elif num>ans: #如果輸入的整數大於答案
        print("太好了！")
    elif num<ans: #如果輸入的整數小於答案
        print("太差了！")
    else: #如果輸入的整數等於答案
        print("回報成功！")
        break #跳出無窮迴圈

#字典(dict):用來儲存[key-value]配對的資料結構
#字典很適合用來表示有對應關係的資料,向式商品和價格的對應

#建立字典:使用大括號{},key和value之間用括號:分隔
d={"appie":1,"banana":2,"cherry":3}
print(d)

#從字典中取得特定key對應的value
#如果key不存在會產生key error 錯誤
d={"appie":1,"banana":2,"cherry":3}
print(d["apple"])
#print(d["apple"]) #錯誤

#遍歷字典:有很多種方法可以走訪字典中的資料
d={"appie":1,"banana":2,"cherry":3}

#方法一:直接遍歷字典,會取得所有key
for key in d:
    print(key) #印出key名稱
    print(d[key]) #印出key對應的value

#方法二:明確使用 keys()方法來取得所有key
for key in d.keys():
    print(key) #印出key名稱
    print(d[key]) #印出key對應的value

#方法三:使用values()方法來取的所有value
for value in d.values():
    print(value) #印出value不知道key是甚麼

#方法四:使用items()方法來取得所有key和value
#這是最常用的方法,因為可以同時存取key跟value
for key,value in d.items():
    print(f"{key}:{value}") #印出key和value

#新增/修改字典內容
#直接指定key對應的value
d={"appie":1,"banana":2,"cherry":3}
d["apple"]=1 #修改[apple]對應的value
print(d)
d["蓮霧"]=4 #新增一個key-value配對
print(d)

#刪除字典內容
d={"appie":1,"banana":2,"cherry":3}
d.pop("appie") #刪除[appie]
#如果要刪掉的key不存在,會出現key error
#這時候可以加上第二個參數,當key不存在時,不嘿有任何變化
popitem=d.pop("apple",None) #刪除[apple]，如果不存在就回傳None 
print(d) #{'banana': 2, 'cherry': 3}
print(popitem) #None