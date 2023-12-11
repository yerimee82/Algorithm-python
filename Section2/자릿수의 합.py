import sys
sys.stdin = open("input.txt", "rt")

x = int(input())
sum_arr = list(map(int, input().split()))

def digit_sum(sum_arr):
    str_list = []
    max_value = 0  # max 변수 이름 변경
    for num in sum_arr:
        new_arr = list(str(num))
        str_list.append(new_arr)
    
    tmp = [sum(int(item) for item in arr) for arr in str_list]
    for i, s in enumerate(tmp):  
        if s > max_value: 
            max_value = s  
            res = [sum_arr[i]]  
        elif s == max_value:
            res.append(sum_arr[i])
    
    return res
    
result = digit_sum(sum_arr)
answer = " ".join(map(str, result))
print(answer)

    