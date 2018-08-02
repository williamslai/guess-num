#guess-num
#產生一個隨機數字(1~100)不要印出來
#讓使用者重複輸入數字去猜
#猜對，你猜對了
#猜錯，要告訴他 把答案大/小
import random
start = input('請輸入隨機數字開始值')
end = input('請輸入隨機數字結束值')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	num = input('請輸入數字： ')
	num = int(num)
	count += 1 #count = count + 1
	if num == r:
		print('你猜對了')
		print('你猜了',count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('你猜了',count, '次')
