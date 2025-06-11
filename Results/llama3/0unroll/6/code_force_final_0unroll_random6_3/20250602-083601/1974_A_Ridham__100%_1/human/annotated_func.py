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
        
    #State: Output State: The list "result" contains n integers, each representing the number of screens required to display the corresponding input pair (x, y). The value of n remains unchanged.
    print('\n'.join(map(str, result)))
    #This is printed: n lines, each containing an integer representing the number of screens required to display the corresponding input pair (x, y)

#Overall this is what the function does:This function calculates and prints the number of screens required to display a series of input pairs (x, y), where x and y are integers representing the dimensions of a display area. It reads an integer t from standard input, followed by t lines, each containing two space-separated integers x and y. For each pair (x, y), it calculates the total space required, determines the number of screens needed to display the pair, and appends this value to a result list. Finally, it prints the result list, containing the number of screens required for each input pair, one value per line.

