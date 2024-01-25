import sys
sys.stdin = open("input.txt", "rt")

# 최적의 해, 정렬 된 배열에서 찾기 => 이분 탐색

n, c = map(int, input().split())
pArr = []
for i in range(n):
    pt = int(input())
    pArr.append(pt)
    
pArr.sort()

lt=1
rt=pArr[-1]
res=0

def Count(len):
    cnt = 1
    ep = pArr[0]
    for i in range(1, n):
        if pArr[i] - ep >= len:
            cnt += 1
            ep = pArr[i]
    return cnt
        
while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= c:
        res=mid
        lt = mid + 1
    else :
        rt = mid - 1 
        
        
print(res)
    
    

