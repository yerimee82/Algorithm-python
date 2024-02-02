import sys
sys.stdin = open("input.txt", "rt")

# 창고 가로의 길이 
l = int(input())

# 각각의 높이
box_ht = list(map(int, input().split()))

# 조정 횟수
m = int(input())

# 정렬
box_ht.sort()
print(box_ht)

for _ in range(m):
    box_ht[0] += 1
    box_ht[-1] -= 1
    box_ht.sort()

print(box_ht[-1] - box_ht[0])

