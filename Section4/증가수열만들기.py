import sys
sys.stdin = open("input.txt", "rt")


# 증가 수열 길이(1씩 증가할 필요 XXX)
n = int(input())

# 수열
arr = list(map(int, input().split()))

lt = 0
rt = n -1
last = 0
res = ""
tmp = []

while lt < rt:
    if arr[lt] > last :
        tmp.append((arr[lt], 'L'))
    if arr[rt] > last :
        tmp.append((arr[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0:
        break
    else :
        res += tmp[0][1]
        last = tmp[0][0]
        # 포인터 번경
        if tmp[0][1] == 'L':
            lt += 1
        else :
            rt -= 1
    tmp.clear()


print(res)
        

