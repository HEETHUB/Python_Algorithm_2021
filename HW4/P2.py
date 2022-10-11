def P2(lst1: list, lst2: list) -> set:
    ### Write code here ###
    result = set()
    for i in range(len(lst1)):
        result.add((lst1[i], lst2[i]))
    ### End of your code ###  

    return result
