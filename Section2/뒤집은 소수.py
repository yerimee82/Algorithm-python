import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
num_arr = list(map(int, input().split()))

def is_Prime(x):
    if x == 1:
        return False
    
    for i in range(2, x):
        if x % i == 0:
            return False
    
    return True

def reverse(x):
    num_str = ''
    for i in reversed(str(x)):
        if i == "0":
            continue
        num_str += i
    
    return int(num_str)
    
result = []
for num in num_arr:
    x_num = reverse(num)
    bool_res = is_Prime(x_num)
    if bool_res == True:
        result.append(x_num)

print(" ".join(map(str, result)))