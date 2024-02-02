import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))
tmp = [0 for _ in range(8)]

for i in range(n):
    for j in range(n):
        if a[i] == 0 and tmp[j] == 0:
            tmp[j] = i+1
            break
        elif tmp[j] == 0:
            a[i] -= 1


for k in tmp:
    print(k, end=' ')