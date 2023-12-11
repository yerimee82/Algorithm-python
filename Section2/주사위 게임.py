import sys
sys.stdin = open("input.txt", "rt")

# 참여하는 사람 수 
n = int(input())


# 상금 계산 함수
def calculatePrize(arr):
    counter = {}
    prize = 0
    for n in arr:
        try: counter[n] += 1
        except: counter[n] = 1
    
    if len(counter) == 3:
        prize = max(counter.keys())
        
    elif len(counter) == 2:
        sameNum = [key for key, value in counter.items() if value == 2]
        prize = 1000 + (sameNum[0] * 100)
    else:
        sameNum = next(iter(counter))
        prize = 10000 + (sameNum) * 1000
    
    return prize  
        
resultArr = []
for i in range(n):
    numArr = list(map(int, input().split()))
    output = calculatePrize(numArr)
    resultArr.append(output)

print(max(resultArr))