from typing import List
def P5(word_num_list: List[list]) -> list:
    ### Modify code here ###
    result = []
    for word in word_num_list:
        result.append(word[0])
    result.sort()
    return result
    ### End of your code ###  
