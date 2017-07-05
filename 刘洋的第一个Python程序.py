import random
secret = random.randint(1,5)
print('刘洋的第一个小游戏')
temp = int(input('请输入数字，来猜一猜游戏，您一共有三次机会'))
guess = int(temp)
times = 0
while (guess != secret) and (times<2):
    if guess == secret:
        print("这么厉害，你竟然三次机会就能猜中")
        print('不过可惜了，猜中也没有奖励的 亲！')
    else:
        if guess > secret:
            print('数值有点大哦！')
        else:
            print('小了，再往大了猜')
        times = times + 1
    temp = input('错了，请重新输入')

