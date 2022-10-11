from typing import List
def P10(word_list: List[str]) -> List[str]:
    ### Modify code here ###
    result = []
    for word in word_list:
        if word[0] == 'a' or word[0] == 'A':
            result.append(word)
    return result
    ### End of your code ###  
