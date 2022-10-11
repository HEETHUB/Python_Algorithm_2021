def P9(vector1: dict, vector2: dict) -> dict:
    ### Write code here ###
    result = 0
    for key in vector2.keys():
        if key in vector1:
            result += vector1[key]*vector2[key]
    ### End of your code ###      
    return result