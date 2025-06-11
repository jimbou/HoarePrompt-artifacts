#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing two space-separated integers x and y (0 <= x, y <= 99).
    n = int(input())
    result = []
    for _ in range(n):
        x, y = list(map(int, input().split()))
        
        space_x = x * 1
        
        space_y = y * 4
        
        total_space = space_y + space_x
        
        if y % 2 == 0:
            screen_require_for_y = y // 2
        else:
            screen_require_for_y = y // 2 + 1
        
        remaining_cells = 15 * screen_require_for_y - space_y
        
        if space_x <= remaining_cells:
            result.append(screen_require_for_y)
        else:
            extra_space = space_x - remaining_cells
            if extra_space % 15 == 0:
                extra_screen = extra_space // 15
            else:
                extra_screen = extra_space // 15 + 1
            result.append(extra_screen + screen_require_for_y)
        
    #State: Output State: The list 'result' contains n integers, each representing the total number of screens required for the corresponding input pair (x, y). The value of 'n' remains unchanged.
    print('\n'.join(map(str, result)))
    #This is printed: The total number of screens required for each input pair (x, y), separated by newline characters

#Overall this is what the function does:This function calculates and returns the total number of screens required for each input pair of integers (x, y), where x and y represent the number of cells required for the x and y coordinates, respectively. The function takes as input a series of pairs of integers (x, y) from standard input, where the number of pairs is specified by an initial integer t. For each pair, it calculates the total number of screens required based on the number of cells required for the y coordinate and the remaining cells available for the x coordinate. If the x coordinate requires more cells than available, it calculates the additional screens needed. The function returns a list of integers, each representing the total number of screens required for the corresponding input pair (x, y).

