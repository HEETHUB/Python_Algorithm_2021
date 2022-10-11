def P8(vector1: dict, vector2: dict) -> dict:
    ### Write code here ###
    result = vector1
    for key in vector2.keys():
        if key in result:
            result[key] += vector2[key]
            if result[key] == 0:
                result.pop(key)
        else:
            result[key] = vector2[key]
    ### End of your code ###      
    return result