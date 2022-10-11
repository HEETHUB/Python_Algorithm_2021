def P4(dct: dict) -> str:
    ### Write code here ###
    result = None
    for key, value in dct.items():
        if result == None:
            result = key
        elif value > dct[result]:
            result = key
    ### End of your code ###  

    return result
