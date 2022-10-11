def P2(n: int) -> bool:
    # write your code below
    binN = str(bin(n))
    i = 3
    ans = binN[2]
    while i < len(binN):
        if binN[i] == ans:
            return False
        else:
            ans = binN[i]
            i += 1
    return True