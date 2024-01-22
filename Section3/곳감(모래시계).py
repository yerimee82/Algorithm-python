import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

m = int(input()) # 회전 명령

for _ in range(m):
    h, v, t = map(int, input().split())
    if v == 0:  # 왼쪽 회전 
        for _ in range(t):
            arr[h-1].append(arr[h-1].pop(0))
    else: # 오른쪽 회전 
        for _ in range(t):
            arr[h-1].insert(0, arr[h-1].pop())
        

s=0
e=n-1
res = 0
for i in range(n):
    for j in range(s,e+1):
        res += arr[i][j]
        
    if i < n//2:
        s += 1
        e -= 1
    else :
        s -= 1
        e += 1

print(res)
        