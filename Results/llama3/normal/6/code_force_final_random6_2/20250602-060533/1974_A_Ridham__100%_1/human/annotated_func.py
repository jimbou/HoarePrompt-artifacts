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
        
    #State: `n` is 0, `result` is a list containing `n` elements, each of which is either `screen_require_for_y` if `space_x` is less than or equal to `15 * screen_require_for_y - space_y`, or `extra_screen + screen_require_for_y` if `space_x` is greater than `15 * screen_require_for_y - space_y`, `x` is an integer between 0 and 99, `y` is an integer between 0 and 99, `space_x` is equal to `x`, `space_y` is equal to 4 times `y`, `total_space` is equal to 5 times `y` plus `x`, `screen_require_for_y` is either half of `y` (integer division) if `y` is even or `y // 2 + 1` if `y` is odd, `remaining_cells` is equal to `15 * screen_require_for_y - space_y`, and stdin is empty.
    print('\n'.join(map(str, result)))
    #This is printed: an empty string

#Overall this is what the function does:Calculates and prints the minimum number of screens required to display a given number of cells, considering the space requirements for both x and y cells, and handles cases where the space required for x cells exceeds the available space on the screens required for y cells.

