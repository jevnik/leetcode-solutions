def isValid(s: str) -> bool:
        temp = []
        dic = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
    
        for j in range(len(s)):
            
            if s[j] in dic.keys():
                temp.append(s[j])
                
            else:
                if len(temp) == 0:
                    return False
                
                if s[j] == dic.get(temp[-1]):
                    temp.pop()
                
                else:
                    return False
           
        if len(temp) == 0:
            
            return True
    
        else:
            return False