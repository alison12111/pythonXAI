# len:取得字典中有都少組key-value配對
d = {"appie": 1, "banana": 2, "cherry": 3}
print(len(d))  # 3.字典中有三組key-value配對

# 檢查某個key是否存在於字典中
# 使用前先檢查可以避免keyError 錯誤
d = {"appie": 1, "banana": 2, "cherry": 3}
print("apple" in d)  # True 存在
print("apple" in d)  # False 不存在

# 檢查某個元素有沒有在list中
# 使用in可以快速檢查某個元素是否存在於list中
l = [1, 2, 3, 4, 5]
print(1 in l)  # True,3在list中

# 比較複雜的dict
d = {"a": [1, 2, 3], "b": {"c": 4, "d": 5}}
print(d["a"])  # [1,2,3]
print(d["a"][0])  # 1
print(d["b"])  # {"c":4,"d":5}
print(d["b"]["c"])  # 4

# 成績登記系統,key是學生名字,value是學生成績,每個科目有3個成績
grade = {
    "小明": {"國語": [90, 80, 70], "數學": [85, 75, 65], "英文": [95, 85, 95]},
    "李四": {"國語": [88, 78, 68], "數學": [83, 73, 63], "英文": [93, 83, 93]},
    "王五": {"國語": [86, 76, 66], "數學": [81, 71, 61], "英文": [91, 81, 71]},
}

# 取得小明的成績
print(grade["小明"]["數學"])  # [85,75,65]
# 取得李四的第一次英文成績成績
print(grade["李四"]["英文"][0])  # 93
# 取的王武的第二次國文成績
print(grade["王五"]["國文"][1])  # 76#[88,78,68]
