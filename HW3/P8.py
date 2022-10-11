from typing import List
def P8(L1: List[int], L2: List[int]) -> List[int]:
    ### Modify code here ###
    result = []
    for i in range(len(L1)):
        result.append(max(L1[i], L2[i]))
    return result                
    ### End of your code ###  
           
                     
                     
                    