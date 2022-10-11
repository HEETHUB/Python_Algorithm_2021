def P3(s: str) -> int:
    ### Modify code here ###
    result = ''
    numbers = {'zero' : '0', 
               'one' : '1', 
               'two' : '2',
               'three' : '3', 
               'four' : '4', 
               'five' : '5', 
               'six' : '6', 
               'seven' : '7', 
               'eight' : '8', 
               'nine' : '9'}
    i = 0
    while i < len(s):
        if ord(s[i]) >= 97:
            j = i + 1
            while j <= len(s):
                if j == len(s):
                    result += numbers[s[i:]]
                    break
                elif s[i:j] in numbers:
                    result += numbers[s[i:j]]
                    break
                else:
                    j += 1
            i = j
        else:
            result += s[i]  
            i += 1
    return int(result)
                    
    ### End of your code ###