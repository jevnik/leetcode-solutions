def add(a,b):
    a = a[::-1]
    b = b[::-1]
    acc = 0
    pow = 0
    
    for e in a:
        acc += int(e) * 2**pow
        pow += 1
    
    pow = 0
    for e in b:
        acc += int(e) * 2**pow
        pow += 1
    
        return bin(acc)[2:]



print(add('111','1'))