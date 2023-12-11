import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())

max = 0
cnt = 0
dic = {}

for i in range(1, n+1):
    for j in range(1, m+1):
        sum = i + j
        if sum in dic:
            dic[sum] += 1
        else:
            dic[sum] = 1 

for key, value in dic.items():
    if value > max:
        max = value
              
for key, value in dic.items():
    if value == max:
        print(key, end=" ")