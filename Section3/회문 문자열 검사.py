import sys
sys.stdin = open("input.txt", "rt")

def checkFrontBackSame(s, idx):
    arr1 = list(s.lower())
    arr2 = list(reversed(arr1))
    
    print(f"#{idx} ", end="")
    if arr1 == arr2:
        print("YES")
    else:
        print("NO")
    
n = int(input())
for i in range(n):
    sentence = input() 
    checkFrontBackSame(sentence, i+1)