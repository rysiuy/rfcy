import random
ssq = []
nums_blue = random.randint(1,16)
while True and len(ssq)<6:
    nums = random.randint(1,33)
    if nums in ssq:
        pass
    else:
        ssq.append(nums)
        ssq.sort()
print(ssq,'+',nums_blue)   
