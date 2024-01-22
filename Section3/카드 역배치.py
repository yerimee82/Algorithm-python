import sys
sys.stdin = open("input.txt", "rt")

def changePosition(x, y, arr):
    newArr = arr[x-1:y]
    re_arr = newArr[::-1]
    for i in range(x-1, y):
        arr[i] = re_arr[i-x+1]
    
    return arr
    
        
numArr = [i for i in range(1,21)]   
for _ in range(10):
    a, b = map(int, input().split())
    result = changePosition(a, b, numArr)

print(result)



