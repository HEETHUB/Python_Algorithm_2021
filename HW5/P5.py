def P5(filename: str) -> int:        
    ##### Write your Code Here #####
    with open(filename, 'r') as file:
        ans = None
        for line in file:
            textline = line.split()
            for text in textline:
                if ans == None:
                    ans = len(text)
                else:
                    if len(text) >= ans:
                        ans = len(text)
        return ans
    ##### End of your code #####