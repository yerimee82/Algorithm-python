import sys
sys.stdin = open("input.txt", "rt")

arr = [list(map(int, input().split())) for _ in range(7)]

cnt = 0
for i in range(3):
    for j in range(7):
        tmp = arr[j][i:i+5]
        if tmp == tmp[::-1]:
            cnt += 1
        for k in range(2):
            if arr[i+k][j] != arr[i+4-k][j]:
                break
            else:
                cnt += 1
                

print(cnt)
