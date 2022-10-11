def P3(num:int)->int:
    # write your code below
    ans = '{:032b}'.format(num)
    ans = ans[::-1]
    decimal = 0
    for num in ans:
        decimal = decimal*2 + int(num)
    return decimal