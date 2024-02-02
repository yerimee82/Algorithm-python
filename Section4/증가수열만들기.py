import sys
from collections import deque
sys.stdin = open("input.txt", "rt")


# 증가 수열 길이
n = int(input())

# 수열
arr = list(map(int, input().split()))
arr = deque(arr)

inc = []
str = "L"
s = arr[0]
res = 0
while arr:
    if len(arr) == 1:
        if inc[-1] + 1 == arr[0]:
        else:
            break
    if s + 1 == arr[1]:
        inc.append(s)
        inc.append(arr[1])
        s = arr[1]
        arr.popleft()
        arr.popleft()
        str += "L"
    elif s + 1 == arr[-1]:
        inc.append(s)
        inc.append(arr[-1])
        s = arr[-1]
        arr.pop()
        arr.popleft()
        str += "R"
    else :
        if len(inc) > 1:
            res = len(inc)
            inc = []
        arr.popleft()


print(res, str)
        

