"""
**Instruction**
Please see instruction document.

"""
def P1(parentheses: str) -> bool:        
    ##### Write your Code Here #####
    stack = []
    for i in parentheses : 
        if i == ')' :
            if stack[-1] == '(' :
                stack.pop()
            else : 
                return False 
        elif i == ']':
            if stack[-1] == '[':
                stack.pop()
            else :
                return False
        elif i == '}':
            if stack[-1] == '{':
                stack.pop()
            else :
                return False 
        else :
            stack.append(i)
    if stack :
        return False
    else :
        return True
    ##### End of your code #####