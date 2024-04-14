import random

numbers = [random.randint(0,50) for _ in range(500)]

count ={}

for i in numbers:
    if i in count:
        count[i] +=1
    else:
        count[i] = 1

sort = sorted(count.items(), key=lambda x:x[1],reverse=True)

for i in range(3):
    key, value = sort[i]
    print(f"숫자: {key} - 등장 횟수: {value}")