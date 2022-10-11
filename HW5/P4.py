def P4(filename: str) -> list:        
    ##### Write your Code Here #####
    with open(filename, 'r') as file:
        result = []
        line = file.readline()
        while line:
            if line.startswith('#') or line.startswith('//'):
                line = file.readline()
                continue
            result.append(line)
            line = file.readline()
        return result
    ##### End of your code #####