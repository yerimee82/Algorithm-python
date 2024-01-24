import sys
sys.stdin = open("input.txt", "rt")

# 가장 작은 수, 가장 큰 수 구할 때 -> max, min
k, n = map(int, input().split())
arr = []
largest = 0

for _ in range(k):
    mak = int(input())
    arr.append(mak)
    largest = max(mak, largest)

def Count(length):
    cnt = 0
    for i in arr:
        cnt += i // length
    return cnt
        

lt = 1
rt = largest
res = 0
while lt<=rt:
    mid = (lt + rt) // 2
    if Count(mid) >= n:
        res = mid
        lt = mid + 1
    else :
        rt = mid - 1

print(res)
    

    


        