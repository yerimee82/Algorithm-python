import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
arr = list(map(int, input().split()))
sum = 0

for i in range(n):
    sum += arr[i]

avg = round(sum/n)
cloest_num = arr[0]

for idx, x in enumerate(arr):
    tmp = abs(avg - x)
    if tmp < cloest_num:
        cloest_num = tmp
        score = x
        res = idx + 1
    elif tmp == cloest_num:
        if x > score:
            score = x
            res = idx + 1

print(avg, res)
        
        