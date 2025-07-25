# 🐍 今天的 Python 小筆記

## 🔢 1. `len()` 是什麼？

`len()` 是用來算「有幾個字」的工具！

```python
print(len("apple"))  # 結果是 5，因為 "apple" 有 5 個字母
print(len(","))      # 結果是 1，因為只有一個符號
```

---

## 📦 2. `type()` 是什麼？

`type()` 可以告訴我們「這是什麼東西」！

```python
print(type(1))        # 整數 → int
print(type(1.0))      # 小數 → float
print(type("apple"))  # 字串 → str
print(type(True))     # 布林值（對或錯）→ bool
```

---

## 🔁 3. 變來變去：型態轉換

有時候我們想把數字變成字，或把小數變成整數！

```python
print(int(1.0))     # 小數變整數
print(float(1))     # 整數變小數
print(str(1))       # 整數變字串
print(bool(1))      # 整數變布林值
print(float("1.234"))  # 字串變小數
```

⚠️ 有些不能轉會報錯喔：

```python
# print(int("hello")) → 會出錯，因為 "hello" 不是數字
```

---

## ⌨️ 4. `input()`：讓使用者輸入東西

```python
a = input("請輸入一個數字：")
print(int(a) + 10)
```

💡 用 `input()` 得到的東西會是字串，要算數學時記得先轉成數字！

---

## ⭕ 5. 計算圓面積的小練習

```python
r = float(input("請輸入圓的半徑："))
pi = 3.14
area = pi * r * r
print(f"圓的面積是：{area}")
```

---

## 💬 6. Streamlit 的顯示工具

Streamlit 是一個可以做「網頁小工具」的東西！

```python
st.write("這是一般的內容")
st.text("這是純文字")
st.markdown("可以做**粗體**、*斜體*、[連結](網址)")
st.title("大標題")
st.info("資訊訊息")
st.success("成功的訊息")
st.warning("警告訊息")
st.error("錯誤訊息")
```

---

## 🔍 7. 比大小和真假判斷

```python
print(1 == 1)  # True，因為一樣
print(1 != 1)  # False，不一樣才是對
print(1 > 1)   # False
print(1 <= 1)  # True
```

---

## ✅ 8. 邏輯運算子（真假配對）

```python
print(True and True)    # 兩個都對，才會是 True
print(True or False)    # 有一個對就會是 True
print(not True)         # 反過來，變 False
```

---

## 📐 9. 計算順序（運算優先）

1. 小括號 ( )
2. 次方 \*\*
3. 乘除（\*/ // %）
4. 加減（+ -）
5. 比較（< > == 等等）
6. not
7. and
8. or

---

## 🔐 10. 判斷密碼（if 判斷式）

```python
password = input("請輸入密碼：")

if password == "123456":
    print("密碼正確")
elif password == "123456789":
    print("密碼正確")
else:
    print("密碼錯誤")
```

💡 `if` 是「如果」，`elif` 是「或者如果」，`else` 是「其他的情況」。

---

## 🔢 11. 數字輸入 + 成績判斷（Streamlit）

```python
score = st.number_input("請輸入你的分數：", step=1, min_value=0, max_value=100)

if score >= 90:
    st.write("你的成績很好！")
elif score >= 80:
    st.write("你的成績一般")
elif score >= 70:
    st.write("你的成績不好")
elif score >= 60:
    st.write("你的成績不太好")
else:
    st.write("你的成績很差")
```
