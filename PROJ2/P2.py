"""
**Instruction**
Please see instruction document.

"""
def P2(stock_price: list) -> list:        
    ##### Write your Code Here #####
    L = []
    for i in range(len(stock_price)):
        L.append(0)
        j = i+1
        while j < len(stock_price):
            if stock_price[j] > stock_price[i]:
                L[i] = j-i
                break
            else:
                j += 1               
    return L
    ##### End of your code #####


