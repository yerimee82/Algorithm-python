import sys
sys.stdin = open("input.txt", "rt")

T = int(input())  # T 테스트 케이스 수, s 시작 e 끝, k 번째 수

for i in range(T):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    n_arr = sorted(arr[s-1:e])
    print("#%d %d" %(i+1, n_arr[k-1]))




    
    