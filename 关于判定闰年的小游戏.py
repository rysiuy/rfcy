print('刘洋的第二个程序')
temp = input('请输入一个年份来判定是否为闰年:')
year = int(temp)
if year/400 == int(year/400):
     print(temp + '这一年是闰年')
else:
     if year/4 == int(year/4) and year/100 != int(year/100):
          print(temp + '这一年是闰年')
     else:
          print('这一年不是闰年')
