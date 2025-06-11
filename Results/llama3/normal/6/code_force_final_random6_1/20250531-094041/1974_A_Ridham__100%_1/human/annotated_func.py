#State of the program right berfore the function call: stdin contains t+1 inputs: the first input is an integer t (1 <= t <= 10^4), and each of the remaining t inputs is a pair of integers x and y (0 <= x, y <= 99).
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
        
    #State: `n` is an integer equal to 0, `result` is a list containing either the value of `screen_require_for_y` or the sum of `screen_require_for_y` and `extra_screen` for each input pair of integers x and y, `stdin` is empty.
    print('\n'.join(map(str, result)))
    #This is printed: (nothing, an empty output)

#Overall this is what the function does:This function reads t+1 inputs from stdin, where t is an integer followed by t pairs of integers x and y. It calculates the minimum number of screens required to display each pair of integers, considering the space requirements for x and y, and appends the result to a list. The function then prints the list of results, one value per line, and leaves stdin empty.

