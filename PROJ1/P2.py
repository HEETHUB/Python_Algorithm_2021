def P2(n: int) -> bool:        
    ##### Write your Code Here #####
    for i in range(2, n+1):
        if n % i == 0:
            m = n // i
            for j in range(2, m+1):
                if m % j == 0:
                    if m / j == 1:
                        return True
                    else:
                        return False
    return False
    ##### End of your code #####