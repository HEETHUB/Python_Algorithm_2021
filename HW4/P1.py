def P1(lst: list) -> set:
    ### Write code here ###
    result = set()
    no = []
    for ele in lst:
        if ele in no:
            result.add(ele)
        else:
            no.append(ele)
    ### End of your code ###  

    return result

