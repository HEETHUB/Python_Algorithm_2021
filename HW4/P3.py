def P3(dct: dict) -> int:
    ### Write code here ###
    S = set()
    for key, value in dct.items():
        S.add(value)
    
    ### End of your code ###  

    return len(S)
