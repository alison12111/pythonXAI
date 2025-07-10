# 連續使用if跟使用if elif else的差別
# elif可以排除前面有判斷過的條件，所以縮短判斷條件的複雜度，也節省了時間
# 但是如果是使用多個if來做獨立判斷，則每個if都會被執行，所以效率較低

# for 迴圈
# for 會搭配 in 來使用，in 後面接一個有範圍的東西
# range(5) 會產生 0, 1, 2, 3, 4，不包含5
# i 是迴圈的變數可以自己取名
# 迴圈變數每回合會從範圍裡面取一個資料出來
for i in range(5):
    print(i)
    print("Hello")

# range 可以設定起始值與結束值, 但不會包含結束值
# range(1, 5) 會產生 1, 2, 3, 4
for i in range(1, 5):
    print(i)

# range 可以設定起始值、結束值與間隔值, 但不會包含結束值
# range(1, 10, 2) 會產生 1, 3, 5, 7, 9
for i in range(1, 10, 2):
    print(i)
