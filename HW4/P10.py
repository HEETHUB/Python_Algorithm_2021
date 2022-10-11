def P10(words: set, query_word: str) -> bool:
    ### Write code here ###
    result = False
    for word in words:
        resultHelp = 0
        if len(word) == len(query_word):
            for i in range(len(word)):
                if word[i] != query_word[i]:
                    resultHelp += 1
            if resultHelp == 1:
                result = True
    ### End of your code ###      

    return result