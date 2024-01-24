import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
arr = list(map(int, input().split()))
nArr = sorted(arr)

lt=0
rt=n-1

while lt<=rt:
    mid = (lt+rt) // 2
    if m == nArr[mid]:
        print(mid+1)
        break
    elif m > nArr[mid]:
        lt = mid+1
    else:
        rt = mid-1



    
    
        
