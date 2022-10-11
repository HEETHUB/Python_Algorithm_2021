def P5(dct: dict) -> list:
    ### Write code here ###
    result = []
    resultHelp = set()
    for key, value in dct.items():
        if value in resultHelp:
            result.append(value)
        else:
            resultHelp.add(value)
    ### End of your code ###  

    return result
