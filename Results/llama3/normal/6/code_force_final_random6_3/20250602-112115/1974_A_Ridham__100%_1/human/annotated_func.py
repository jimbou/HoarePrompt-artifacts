#State of the program right berfore the function call: stdin contains t+1 inputs: the first input is an integer t (1 <= t <= 10^4) and the rest t inputs are pairs of integers x and y (0 <= x, y <= 99).
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
        
    #State: `n` is an integer equal to 0, `result` is a list containing either `screen_require_for_y` or the sum of `extra_screen` and `screen_require_for_y` for each input pair of integers `x` and `y`, stdin contains 0 inputs: pairs of integers `x` and `y`, `_` is `n`, `x` is an integer, `y` is an integer, `space_x` is an integer equal to `x`, `space_y` is an integer equal to 4y, `total_space` is an integer equal to 5x + 4y. If `y` is even, `screen_require_for_y` is an integer equal to `y // 2`. If `y` is odd, `screen_require_for_y` is an integer equal to `y // 2 + 1`. `remaining_cells` is an integer equal to 15 * `screen_require_for_y` - `space_y`. If `space_x` is less than or equal to `remaining_cells`, the current value of `space_x` is less than or equal to the current value of `remaining_cells`. Otherwise, `extra_space` is an integer equal to `space_x` - `remaining_cells` which is equal to `space_x` - (15 * `screen_require_for_y` - `space_y`). If `extra_space` is a multiple of 15, `extra_screen` is an integer equal to `extra_space // 15` which is equal to (`space_x` - (15 * `screen_require_for_y` - `space_y`)) // 15. Otherwise, `extra_screen` is an integer equal to `extra_space // 15 + 1` which is equal to (`space_x` - (15 * `screen_require_for_y` - `space_y`)) // 15 + 1.
    print('\n'.join(map(str, result)))
    #This is printed: A list of integers where each integer is either screen_require_for_y or the sum of extra_screen and screen_require_for_y for each input pair of integers x and y

#Overall this is what the function does:Calculates and prints the minimum number of screens required to display a given number of cells, considering the available space on each screen and the number of cells that can fit in the remaining space.

