def P4(info: list) -> str:        
    ##### Write your Code Here #####
    result = ''
    if info[0] == 'MALE':
        if info[1] >= 2000:
            gender = '3'
        elif info[1] >= 1900:
            gender = '1'
        else:
            gender = '9'
    else:
        if info[1] >= 2000:
            gender = '4'
        elif info[1] >= 1900:
            gender = '2'
        else:
            gender = '0'
            
    for i in range(1, 4):
        if info[i] < 10:
            info[i] = '0' + str(info[i])
            result += info[i]
        else:
            info[i] = str(info[i])[-2:]
            result += info[i]
    result += gender
    return result
    
    ##### End of your code #####