import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
arr = [0] * (n+1)
cnt = 0
for i in range(2, len(arr)):
    if arr[i] == 0:
        cnt += 1
        for j in range(i, len(arr), i):
            arr[j] = 1


print(cnt)