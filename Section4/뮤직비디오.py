import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
music = list(map(int, input().split()))


def get_sum(capacity):
    cnt=1
    sum=0
    for k in music:
        if sum+k > capacity:
            cnt += 1
            sum = k
        else :
            sum += k
    return cnt
           
lt = 1
rt = sum(music)
res = 0
while lt<=rt:
    mid = (lt + rt) // 2
    if get_sum(mid) <= m :
        res = mid
        rt = mid - 1
    else :
        lt = mid + 1
       
        
print(res)
