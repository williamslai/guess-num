#guess-num
#產生一個隨機數字(1~100)不要印出來
#讓使用者重複輸入數字去猜
#猜對，你猜對了
#猜錯，要告訴他 把答案大/小
import random
r = random.randint(1, 100)
while True:
	num = input('請輸入數字： ')
	num = int(num)
	if num == r:
		print('你猜對了')
		break
	else:
		if num > r:
			print('比答案大')
		else:
			print('比答案小')
