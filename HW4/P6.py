def P6(dct1: dict, dct2: dict) -> dict:
    ### Write code here ###
    result = {}
    for key, value in dct1.items():
        if key in dct2 and value == dct2[key]:
            result[key] = value
    ### End of your code ###  

    return result
