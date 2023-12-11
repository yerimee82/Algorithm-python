import sys
sys.stdin = open("input.txt", "rt")

# N개의 문제
n = int(input())
arr = list(map(int, input().split()))

flag = False
for i in range(n):
    if arr[i] == 1 and flag == False:
        flag = True
    elif arr[i] == 0 and flag == True:
        flag = False
    elif arr[i] == 1 and flag == True:
        arr[i] = arr[i-1] + 1

print(sum(arr))