def isPalindrome(self, s: str) -> bool:
        arr = []
        for chr in s :
            if chr.isalnum():
                arr.append(chr.lower())

        reverse = arr[::-1]
        if arr == reverse:
            return True
        else:
            return False