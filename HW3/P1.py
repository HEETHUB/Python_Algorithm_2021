from typing import List
def P1(num_list: List[int]) -> List[int]:
    ### Modify code here ###
    num_list.sort()
    num_list.remove(1234)
    num_list += [4321, 2222]
    num_list.insert(1, 1111)
    return num_list
    ### End of your code ###
    