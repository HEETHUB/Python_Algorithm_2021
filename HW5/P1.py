def P1(filename: str) -> list:        
    ##### Write your Code Here #####
    with open(filename, 'r') as text:
        result = []
        for line in text:
            result.append(line.split())
    return result
    ##### End of your code #####

