from collections import deque
def isPalindrome(self, s: str) -> bool:
        # 덱 자료형 사용
        arr = deque()
        
        for chr in s :
            if chr.isalnum():
                arr.append(chr.lower())

        while len(arr) > 1 :
            if arr.popleft() != arr.pop():
                return False
        
        return True