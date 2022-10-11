def P3(filename: str) -> list:        
    ##### Write your Code Here #####
    with open(filename, 'r') as file:
        result = []
        for line in file:
            result.append(line)
        result.reverse()
        return result
    ##### End of your code #####
    