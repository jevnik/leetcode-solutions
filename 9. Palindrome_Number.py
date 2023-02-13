def isPalindrome(x: int) -> bool:
        x = str(x)
        y = str(x)
        y = y[::-1]
        if x == y:
            return True
        else:
            return False
    
print(isPalindrome(121))