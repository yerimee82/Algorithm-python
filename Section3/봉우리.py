import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.insert(0, [0]*n)
arr.append([0]*n)

for x in arr:
    x.insert(0, 0)
    x.append(0)
        
res = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        x = arr[i][j]
        # 왼쪽 오른쪽 비교
        if arr[i][j-1] < x and arr[i][j+1] < x and arr[i-1][j] < x and arr[i+1][j] < x:
            res += 1
        

print(res)


# 다른 방법 
# all() -> 모든 조건을 다 검사함
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# if all(arr[i][j] > arr[i+dx[k]][j+i+dy[k]] for k in range(4))