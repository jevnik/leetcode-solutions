def numberOfSteps(self, num: int) -> int:
    brojac = 0
    while num > 0: 
        if num % 2 == 0:
            brojac = brojac +1
            num = num / 2
        else: 
            num = num -1
            brojac = brojac+1
    return brojac

    