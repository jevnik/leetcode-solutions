def maximumWealth(accounts) -> int:
    s = 0
    for i in range(len(accounts)):
        if sum(accounts[i]) > s:
            s = sum((accounts[i]))
    return s