def plusOne(digits):
    acc = 0
    
    for i in range(len(digits)):
        acc += digits[i] * (10**(len(digits)-(i+1)))
        res = acc + 1
    res_list = list(str(res))
    for e in range(len(res_list)):
        res_list[e] = int(res_list[e])
    return res_list