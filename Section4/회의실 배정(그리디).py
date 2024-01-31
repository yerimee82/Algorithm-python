import sys
sys.stdin = open("input.txt", "rt")

# 회의 수 
n = int(input())

arr = []
# 회의 시간 입력 
for i in range(n):
    s, e = map(int, input().split())
    arr.append((s, e))


# 정렬
arr.sort(key=lambda x : (x[1], x[0]))


et=0
cnt=0
for s, e in arr:
    if s >= et:
        et = e
        cnt +=1 

print(cnt)