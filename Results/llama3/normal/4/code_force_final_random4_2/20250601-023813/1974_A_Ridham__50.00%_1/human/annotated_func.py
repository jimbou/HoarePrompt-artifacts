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
            if space_x % 15 == 0:
                extra_screen = space_x // 15
            else:
                extra_screen = extra_space // 15 + 1
            result.append(extra_screen + screen_require_for_y)
        
    #State: n is 0, result is a list containing either screen_require_for_y or the sum of extra_screen and screen_require_for_y repeated t times, x is an integer, y is an integer, space_x is x, space_y is 4 times y, total_space is 5 times x plus 4 times y, remaining_cells is 15 times screen_require_for_y minus 4 times y, stdin is empty. If y is even, screen_require_for_y is equal to half of y. If y is odd, screen_require_for_y is half of y plus 1. If space_x is less than or equal to remaining_cells, result contains screen_require_for_y. Otherwise, result contains the sum of extra_screen and screen_require_for_y, where extra_screen is either a non-negative integer if space_x is a multiple of 15, or the ceiling of extra_space divided by 15 if space_x is not a multiple of 15.
    print('\n'.join(map(str, result)))
    #This is printed: screen_require_for_y repeated t times if space_x is less than or equal to remaining_cells, otherwise the sum of extra_screen and screen_require_for_y repeated t times (where screen_require_for_y is half of y if y is even, half of y plus 1 if y is odd, extra_screen is a non-negative integer if space_x is a multiple of 15, or the ceiling of extra_space divided by 15 if space_x is not a multiple of 15)

#Overall this is what the function does:This function calculates and prints the minimum number of screens required to display a series of input pairs (x, y) on a 15-cell screen, where x and y are integers between 0 and 99. For each pair, it determines the minimum number of screens needed to accommodate the x and y values, considering the screen's 15-cell width and the requirement for y to be displayed in a specific format. The function takes no arguments and returns no value, instead printing the calculated minimum number of screens for each input pair.

