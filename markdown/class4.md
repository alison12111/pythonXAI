## 🧠 今天的 Python 小筆記

### 一、🧱 Streamlit 介面排版與按鈕

#### 1️⃣ 分欄顯示（st.columns）

可以把畫面分成幾欄，像這樣：

```python
col1, col2 = st.columns(2)
col1.button("按鈕1")
col2.button("按鈕2")
```

也可以用比例調整欄位大小：

```python
col1, col2 = st.columns([1, 2])
```

#### 2️⃣ 用 `with` 加上內容

```python
with col1:
    st.write("這是第一欄")
    st.button("按我")
```

#### 3️⃣ 多欄位用 `for` 迴圈自動排

```python
cols = st.columns(4)
for i in range(4):
    with cols[i]:
        st.button(f"按鈕{i+1}")
```

---

### 二、🎮 按鈕和輸入框

#### 📝 文字輸入

```python
text = st.text_input("請輸入文字", value="這是預設文字")
st.write(f"你輸入的文字是:{text}")
```

#### 🧠 記住狀態（session_state）

讓變數按下按鈕後還能記住：

```python
if "ans1" not in st.session_state:
    st.session_state.ans1 = 1

if st.button("加 1"):
    st.session_state.ans1 += 1

st.write(f"ans={st.session_state.ans1}")
```

#### 🔄 重新整理畫面

```python
if st.button("重新整理"):
    st.rerun()
```

---

### 三、🍔 點餐機小專案

#### ✅ 加餐點到購物車

```python
if "order" not in st.session_state:
    st.session_state.order = []

food = st.text_input("請輸入餐點")
if st.button("加入"):
    st.session_state.order.append(food)
```

#### ❌ 刪除餐點

```python
for i in range(len(st.session_state.order)):
    col1, col2 = st.columns(2)
    with col1:
        st.write(st.session_state.order[i])
    with col2:
        if st.button("刪除", key=i):
            st.session_state.order.pop(i)
            st.rerun()
```

---

### 四、🔢 算術指定運算子（+=、-= 等）

| 原本寫法     | 縮寫寫法  | 意思 |
| ------------ | --------- | ---- |
| `a = a + 1`  | `a += 1`  | 加法 |
| `a = a - 1`  | `a -= 1`  | 減法 |
| `a = a * 2`  | `a *= 2`  | 乘法 |
| `a = a / 2`  | `a /= 2`  | 除法 |
| `a = a // 2` | `a //= 2` | 整除 |
| `a = a % 2`  | `a %= 2`  | 餘數 |
| `a = a ** 2` | `a **= 2` | 次方 |

---

### 五、📊 運算順序（誰先算？）

從先到後：

1. 括號 `()`
2. 次方 `**`
3. 乘除整除餘數 `* / // %`
4. 加減 `+ -`
5. 比較 `== != > < >= <=`
6. `not`
7. `and`
8. `or`
9. 算術指定運算子 `+= -= *= ...`

---

### 六、🔁 while 迴圈 + break

#### 🌀 while 會一直重複做某件事，直到條件變 False。

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

#### 🛑 break 會強制跳出迴圈

```python
while True:
    num = int(input("請輸入數字："))
    if num == 0:
        break  # 離開迴圈
```

---

### 七、🎲 隨機數字 random

```python
import random
print(random.randint(1, 6))  # 1 到 6 的整數（包含6）
```

---

### 八、🎯 猜數字遊戲小範例

```python
ans = random.randint(1, 100)

while True:
    num = int(input("猜一個 1 到 100 的數字："))
    if num < 1 or num > 100:
        print("請輸入正確範圍")
    elif num > ans:
        print("太大了")
    elif num < ans:
        print("太小了")
    else:
        print("答對了！")
        break
```

---

### 九、📚 字典 dict（像一本對照表）

#### ✅ 建立字典

```python
d = {"apple": 1, "banana": 2, "cherry": 3}
```

#### 🔍 查找資料

```python
print(d["apple"])  # 找出對應的值
```

#### 🔁 遍歷（走過每一項）

```python
# 方法一
for key in d:
    print(key, d[key])

# 方法二
for key in d.keys():
    print(key)

# 方法三
for value in d.values():
    print(value)

# 方法四（最常用）
for key, value in d.items():
    print(f"{key} : {value}")
```

#### ✏️ 新增或修改

```python
d["apple"] = 10  # 修改
d["watermelon"] = 5  # 新增
```

#### ❌ 刪除

```python
d.pop("apple")  # 刪除一個項目
d.pop("不存在的key", None)  # 不會錯
```
