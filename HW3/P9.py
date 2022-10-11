from typing import List
def P9(n1: int, n2: int) -> List[int]:
    ### Modify code here ###
    result = []
    if n1 >= n2:
        for i in range(n2, n1+1):
            result.append(i)
    elif n1 < n2:
        for i in range(n1, n2+1):
            result.append(i)
    result.sort(reverse = True)
    return result
    ### End of your code ###  
