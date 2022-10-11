def P1(game: list) -> int:        
    ##### Write your Code Here #####
    win = 0
    for match in game:
        if match[1] == 'S':
            if 'R' not in match and 'P' in match:
                win += 1
        if match[1] == 'R':
            if 'P' not in match and 'S' in match:
                win += 1
        if match[1] == 'P':
            if 'S' not in match and 'R' in match:
                win += 1
    return win
    ##### End of your code #####