def longestCommonPrefix(strs) -> str:
        if strs == None or len(strs) == 0:
            return ""
        prva_rijec = min(strs)
        druga_rijec = max(strs)
        rez = ""
        for i in range(len(prva_rijec)):
            if prva_rijec[i] != druga_rijec[i]:
                break
            if prva_rijec[i] == druga_rijec[i]:
                rez = rez + prva_rijec[i]
                
        
        return(rez)

