import sys
sys.stdin = open("input.txt", "rt")

num, t = map(int, input().split())

arr = [int(n) for n in str(num)]
stk = []

cnt = 0


# for n in arr:
#     if stk and cnt == t:
#         break
#     # 스택의 맨 마지막 값보다 넣을 값이 크면 pop 
#     if stk and n > stk[-1]:
#         while stk and n > stk[-1]:
#             if cnt == t :
#                 break
#             stk.pop()
#             cnt += 1
#         stk.append(n)
#     # 스택에 넣는다 
#     else:
#         stk.append(n)
        

# while cnt < t:
#     stk.pop()
#     cnt += 1


for n in arr:
    while stk and t > 0 and n > stk[-1]:
        stk.pop()
        t -= 1
    stk.append(n)

while t > 0:
    stk.pop()
    t-=1

print(''.join(map(str, stk)))
    

