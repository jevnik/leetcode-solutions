def lengthOfLastWord(s: str) -> int:
        words = s. split(' ')
        while words[-1].isalpha() == False:
            words.pop()
        return len(words[-1])