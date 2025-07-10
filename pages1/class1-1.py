#  '''
# 多行註解
# 這邊可以放很多的文字
# '''
# 這是單行註解
# ctrl+?把文字全選可以快速註解，或取消註解
print(1)  # int是整數1,2,3,4,5,6.....
print(1.0)  # float是浮點數
print(1.234)  # float是浮點數
print("apple")  # str字串
print(True)  # 布林值True/False
print(False)  # 布林值True/False

a = 10  # 新增一個儲存空間並取名為a,"="的功能是將右邊的值10存入左邊的a
print(a)  # 在終端機顯示a所存的值
a = "apple"  # 將a的值改為"apple"
print(a)  # 在終端機顯示a所存的值

# 運算子
print(a + a)  # 加法
print(a - a)  # 減法
print(a * a)  # 乘法
print(a / a)  # 除法
print(a // a)  # 整除
print(a % a)  # 取餘數
print(a**a)  # 次方

# 優先順序
# 1.( )括號
# 2.** 次方
# 3.*/ // %  乘 除 取商 取於數

# 字串運算
# print("apple"+"pen") # 字串加法
# print("apple"*3) # 字串乘法

# 練習
a = 10
b = 20
print(a + " " + b)
name = "apple"
age = 18
print(f"My name is {name}, I am {age} years old")  # f-string
# 可以將變數或其他型態的資料放到f字串裡面的{}，這樣就可以在字串中顯示
