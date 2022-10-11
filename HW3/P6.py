from typing import List
def P6(alphabet_list: List[str]) -> int:
    ### Modify code here ###
    i = 0
    while i < len(alphabet_list):
        if alphabet_list[i].isupper() == True:
            return i
        i += 1
    return -1      
    ### End of your code ### 
