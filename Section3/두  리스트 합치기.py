import sys
sys.stdin = open("input.txt", "rt")

result = []

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))


px, py = 0, 0

while px < n and py < m:
    if a[px] <= b[py]:
        result.append(a[px])
        px+=1
    else:
        result.append(b[py])
        py+=1
        
if px < n:
    result = result + a[px:]
if py < m:
    result = result + b[py:]


for x in result:
    print(x, end=" ")
        