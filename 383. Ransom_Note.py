def canConstruct(ransomNote: str, magazine: str) -> bool:
    magazine_list = []
    brojac = 0
    if len(magazine) < len(ransomNote):
        return False
    else:
        for i in range(len(magazine)):
            magazine_list.append(magazine[i])
            

        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine_list:
                brojac = brojac + 1
                magazine_list.remove(ransomNote[i])
            
            if brojac == len(ransomNote):
                return True