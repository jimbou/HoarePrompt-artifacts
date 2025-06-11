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
            if extra_space % 15 == 0:
                extra_screen = extra_space // 15
            else:
                extra_screen = extra_space // 15 + 1
            result.append(extra_screen + screen_require_for_y)
        
    #State: Output State: The final state of the loop is that the variable "result" is a list of integers, where each integer represents the total number of screens required for each pair of inputs (x, y). The value of "n" remains unchanged, and the stdin is empty since all inputs have been read.
    print('\n'.join(map(str, result)))
    #This is printed: A list of integers, where each integer represents the total number of screens required for each pair of inputs (x, y)

#Overall this is what the function does:This function reads a series of input pairs (x, y) from stdin, calculates the total number of screens required for each pair based on specific space requirements, and prints a list of these screen counts. The function takes no explicit parameters but consumes input from stdin, and its output is a list of integers representing the total screens required for each input pair.

