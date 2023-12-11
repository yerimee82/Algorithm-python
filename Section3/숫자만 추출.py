import sys
sys.stdin = open("input.txt", "rt")

s = input()
numArr = []

# 숫자만 추출
for c in list(s):
    if c.isdigit():
        numArr.append(c)

# 하나의 숫자로 변환
s_num = ''
for num in numArr:
    s_num += num

result = int(s_num)

# 약수의 개수 구하기 
cnt = 0
for i in range(1,result+1):
    if result % i == 0:
        cnt += 1

print(result)
print(cnt)
