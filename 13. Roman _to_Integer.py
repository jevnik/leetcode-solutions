def romanToInt(s: str) -> int:
        
        arapski = 0
        
        #  pretvor = {
        #     "I" : 1,
        #     "V" : 5,
        #     "X" : 10,
        #     "L" : 50,
        #     "C" : 100,
        #     "D" : 500,
        #     "M" : 1000,
        # }
        for _ in range(len(s)):
            
            if "CM" in s:
                arapski += 900
                s = s.replace("CM","",1)
            
            if "CD" in s:
                arapski += 400
                s = s.replace("CD","",1)
            
            if "XC" in s:
                arapski += 90
                s = s.replace("XC","",1)
                
            if "XL" in s:
                arapski += 40
                s = s.replace("XL","",1)
            
            if "IX" in s:
                arapski += 9
                s = s.replace("IX","",1)
                
            if "IV" in s:
                arapski += 4
                s = s.replace("IV","",1)
            
            if "I" in s:
                arapski += 1
                s = s.replace("I","",1)
            
            if "X" in s:
                arapski += 10
                s = s.replace("X","",1)
            
            if "L" in s:
                arapski += 50
                s = s.replace("L","",1)
            
            if "C" in s:
                arapski += 100
                s = s.replace("C","",1)
                
            if "D" in s:
                arapski += 500
                s = s.replace("D","",1)
                
            if "M" in s:
                arapski += 1000
                s = s.replace("M","",1)
            
            if "V" in s:
                arapski += 5
                s = s.replace("V","",1)
                
        return arapski


print(romanToInt('XV'))