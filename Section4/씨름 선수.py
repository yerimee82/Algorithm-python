import sys
sys.stdin = open("input.txt", "rt")

# 인원 수 입력
n = int(input())

# 지원자 정보
applicant = []
for _ in range(n):
    h, w = map(int, input().split())
    applicant.append((h, w))


# 정렬
applicant.sort(reverse=True)
    

# 비교
cnt = 0
biggest = 0
for h, w in applicant:
    if w > biggest:
        cnt += 1
        biggest = w

print(cnt)



