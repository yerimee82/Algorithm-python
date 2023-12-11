import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

largest = -454700000
# 행 및 열의 합
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1 += arr[i][j]  # 행의 합
        sum2 += arr[j][i]  # 열의 합
    if sum1 > largest :
        largest = sum1
    if sum2 > largest:
        largest = sum2
    
    
# 대각선의 합
sum1=sum2=0
for i in range(n):
    sum1 += arr[i][i]
    sum2 += arr[i][n-i-1]

if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2
    
print(largest)