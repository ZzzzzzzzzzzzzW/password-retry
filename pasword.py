password = 'a123456'
i = 3 #剩余机会
while i > 0:
	i = i - 1
	pwd = input('请输入密码')
	if pwd == password:
		print('欢迎登陆')
		break #逃出回圈
	else:
		print('密码错误!')
		if i > 0:
			print('还有', i, '次机会')
		else:
			print('账户已锁定！')

