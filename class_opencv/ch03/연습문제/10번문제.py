import random

datas = [random.randint(0,50) for _ in range (500)]

count = {}

for i in datas:
    if i in count:
        count[i] +=1
    else:
        count[i] = 1

sort = sorted(count.items(), key = lambda x:x[1] ,reverse=True )

for i in range(3):
    num, cnt = sort[i]
    print(f"숫자: {num} 중복 횟수: {cnt}")