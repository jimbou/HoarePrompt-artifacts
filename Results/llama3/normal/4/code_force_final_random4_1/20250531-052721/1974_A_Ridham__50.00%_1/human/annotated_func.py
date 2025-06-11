#State of the program right berfore the function call: stdin contains t+1 inputs: first an integer t (1 <= t <= 10^4), then t pairs of integers x and y (0 <= x, y <= 99).
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
        
    #State: `n` is 0, `result` is a list containing either `screen_require_for_y` or the sum of `extra_screen` and `screen_require_for_y` for each pair of integers `x` and `y` in `stdin`, `x` is an integer, `y` is an integer, `space_x` is an integer equal to the last value of `x`, `space_y` is an integer equal to 4 times the last value of `y`, `total_space` is an integer equal to 5 times the last value of `y` plus the last value of `x`, `_` is `n`, `stdin` is empty, `remaining_cells` is an integer equal to 15 times `screen_require_for_y` minus `space_y`, and if `y` is even, `screen_require_for_y` is an integer equal to `y` divided by 2 and `remaining_cells` is an integer equal to 15 times `y` divided by 2 minus 4 times `y`. If `y` is odd, `screen_require_for_y` is an integer equal to `y // 2 + 1` and `remaining_cells` is an integer equal to 15 times (`y // 2 + 1`) minus 4 times `y`. If `space_x` is less than or equal to `remaining_cells`, then `space_x` is less than or equal to `remaining_cells`. Otherwise, `extra_space` is an integer equal to `space_x` minus `remaining_cells`. If `space_x` is a multiple of 15, `extra_screen` is an integer equal to `space_x` divided by 15. If `space_x` is not a multiple of 15, `extra_screen` is an integer equal to `extra_space` divided by 15 plus 1. In all cases, `space_x` is either less than or equal to `remaining_cells` or more than `remaining_cells`.
    print('\n'.join(map(str, result)))
    #This is printed: An empty list

#Overall this is what the function does:Calculates the minimum number of screens required to display a given number of cells, considering the available space on each screen, and prints the results for multiple input pairs.

