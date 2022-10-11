from typing import List
def P7(num_list: List[int]) -> int:
    ### Modify code here ###
    result = 0
    for num in num_list:
        if num >= 0:
            result += num
    return result
    ### End of your code ###  

     