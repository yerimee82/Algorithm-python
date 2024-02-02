import sys
sys.stdin = open("input.txt", "rt")

# 승객 수, 총 무게
n, m = map(int, input().split())

# 몸무게
weight = list(map(int, input().split()))

# 거꾸로 정렬
weight.sort(reverse=True)

# 리스트를 활용한 풀이 
# cnt = 0
# while weight :
        # if len(weight) == 1:
        #         res += 1
        #         break
#     if weight[0] + weight[-1] <= m:
#         weight.pop(0)
#         weight.pop()
#     else:
#         weight.pop(0)
#     cnt += 1

    
        
# 덱을 활용한 풀이
from collections import deque
weight = deque(weight)

res = 0
while weight:
    if len(weight) == 1:
        res += 1
        break
    if weight[0] + weight[-1] <= m:
        weight.popleft()
        weight.pop()
    else:
        weight.popleft()
    res += 1
    
print(res)