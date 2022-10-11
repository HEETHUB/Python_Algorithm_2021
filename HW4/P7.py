def P7(dct: dict) -> int:
    ### Write code here ###
    check = None
    result = 0
    for key, value in dct.items():
        if check == None:
            check = set(value.keys())
        else :
            if check == set(value.keys()):
                result = 1
            else :
                result = 0 
                break        
    ### End of your code ###      
    return result