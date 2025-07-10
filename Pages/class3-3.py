print([])  # 這是一個空的list
print([1, 2, 3])  # 這是一個包含3個三個元素的list
print([1, 2, 3, "a", "b", "c"])  # 這是一個包含6個元素的list
print([1, 2, 3, ["a", "b", "c"]])  # 這是一個包含4個元素的list
print([1, True, "a", False])  # 這是一個包含4個元素的list

# list 讀取元素，元素的index從0開始
L = [1, 2, 3, "a", "b", "c"]
print(L[0])  # 1
print(L[1])  # 2
print(L[2])  # 3
print(L[3])  # "a"

L = [1, 2, 3, "a", "b", "c"]
# 就是取index 0到最後，每次取2個元素，所以是[1, 3, 'b']
print(L[::2])
# 就是取index 1到3的元素，不包含index 4，所以是[2, 3, 'a']
print(L[1:4])
# 　就是取index 1到3的元素，不包含index 4，並且每次取2個元素，所以是[2, 3, 'a']
print(L[1:4:2])
# 　跟range一樣的用法，只是符號不同

# list　取長度，也就是list５中有幾個元素，不是index的最大值
L = [1, 2, 3, "a", "b", "c"]
print(len(L))  # 6

# list 走訪元素
# 可以透過取得index的方式來找到list中的資料
# 也可以直接把list當作一個範圍來取的資料
# 這兩種方式都可以，但是看使用的情境是否需要index來決定要用哪一種方式
L = [1, 2, 3, "a", "b", "c"]
for i in range(0, len(L), 2):
    print(L[i])

for i in L:
    print(i)

# list 修改元素
# 可以透過index來修改list中的元素
L = [1, 2, 3, "a", "b", "c"]
L[0] = 2  # 把index 0的元素改成2
print(L)

# call by value
a = 1
b = a
b = 2
print(a, b)  # a還是1，b變成2

# call by reference
a = [1, 2, 3]
b = a  # 把a跟b指向同一個記憶體位置，所以改變b的值，a也會跟著改變
b[0] = 2
print(a, b)

a = [1, 2, 3]
b = a.copy()  # 複製a的值給b跟a指向不同的記憶體位置
b[0] = 2
print(a, b)

# list的append，也就是在list最後面加入新的元素
L = [1, 2, 3]
L.append(4)  # 把4加到L的最後面
print(L)

# list的移除方式有兩種
# 1. 使用remove，可以移除指定的元素
L = ["a", "b", "c", "d", "a"]
L.remove("a")  # 移除第一個出現的"a"
# 代表remove會從頭開始找，找到第一個符合的元素就會移除
# 如果想要移除所有符合的元素，可以使用迴圈
for i in L:
    if i == "a":
        L.remove(i)
# 2. 使用pop，可以移除指定的index元素
L = ["a", "b", "c", "d", "a"]
L.pop(0)  # 移除index 0的元素
# 代表pop會移除指定的index元素
# 如果不指定index，就會移除最後面的元素
L.pop()  # 移除最後面的元素
print(L)

# sort：將list中的元素進行排序，預設是由小到大( 升序排列 )
# 　注意：這個方法會直接修改原本的list，不會產生新的list
L = [1, 2, 3, 4, 5]
L.sort()
print(L)

# open() 開啟模式
# r - 讀取模式、檔案必須存在
# w - 寫入模式、檔案不存在會自動建立
# a - 附加模式、檔案不存在會自動建立
# r+ - 讀取與寫入模式、檔案必須存在
# w+ - 讀取與寫入模式、檔案不存在會自動建立
# a+ - 讀取與附加模式、檔案不存在會自動建立

# 開啟檔案
# 絕對路徑 C:\Users\Phoebe\Desktop\pythonXAI\pages\class1-1.py
# 相對路徑 pages\class1-1.py
f = open("pages\class1-1.py", "r", encoding="utf-8")
content = f.read()  # 讀取內容
print(content)  # 印出內容
f.close()  # 關閉檔案
######################################
with open("pages\class1-1.py", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)  # 印出內容
# 不用寫 f.close(), with 幫你自動關閉

# 字串的小工具，用來檢查字串最後是不是某個結尾
filename = "class1-1.md"
print(filename.endswith(".md"))  # True
filename2 = "notes.txt"
print(filename2.endswith(".md"))  # False
