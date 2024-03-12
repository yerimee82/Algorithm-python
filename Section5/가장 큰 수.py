import sys
sys.stdin = open("input.txt", "rt")

num, n = map(int, input().split())

arr = [int(n) for n in str(num)]
stk = []

cnt = 0


for n in arr:
    if cnt == n:
        print(stk)
    # 스택의 맨 마지막 값보다 넣을 값이 크면 pop 
    if stk and n > stk[-1]:
        while stk and n > stk[-1]:
            if cnt == n :
                print(stk)
                break
            stk.pop()
            cnt += 1
        stk.append(n)
    # 스택에 넣는다 
    else:
        stk.append(n)
    
    
    print(stk, cnt)
    

