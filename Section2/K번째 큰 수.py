import sys
sys.stdin = open("input.txt", "rt")

N, K = map(int, input().split()) #N 카드 개수, K 번째 큰 수 
arr = list(map(int, input().split()))
sum = 0
sum_arr = []

for i in range(N):
    for j in range(i+1,N):
        for m in range(j+1, N):
            sum = (arr[i] + arr[j] + arr[m])
            sum_arr.append(sum)

answer = list(sorted(set(sum_arr), reverse=True))
print(answer[K-1])


            

