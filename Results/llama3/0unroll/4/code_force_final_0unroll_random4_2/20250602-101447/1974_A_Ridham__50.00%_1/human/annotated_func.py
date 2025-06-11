#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing two integers x and y (0 <= x, y <= 99).
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
            if space_x % 15 == 0:
                extra_screen = space_x // 15
            else:
                extra_screen = extra_space // 15 + 1
            result.append(extra_screen + screen_require_for_y)
        
    #State: Output State: The list "result" contains n integers, each representing the total number of screens required for a given input pair (x, y). The value of n remains unchanged.
    print('\n'.join(map(str, result)))
    #This is printed: The total number of screens required for each input pair (x, y), with each result on a new line

#Overall this is what the function does:This function calculates and returns the total number of screens required for each input pair of integers (x, y), where x and y represent the number of cells required for a specific task. The function takes as input a series of pairs (x, y) from standard input, processes each pair, and outputs the total number of screens required for each pair, one result per line. The function handles cases where the total space required for y is not enough to accommodate x, and calculates the additional screens needed. The function returns a list of integers, each representing the total number of screens required for a given input pair (x, y).

