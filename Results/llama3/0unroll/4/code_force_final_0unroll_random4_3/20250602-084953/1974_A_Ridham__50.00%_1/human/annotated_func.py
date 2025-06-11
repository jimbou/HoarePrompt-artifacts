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
        
    #State: Output State: The list "result" contains n integers, each representing the number of screens required to display the corresponding input values of x and y. The value of n remains unchanged.
    print('\n'.join(map(str, result)))
    #This is printed: A list of n integers, each representing the number of screens required to display the corresponding input values of x and y

#Overall this is what the function does:This function calculates and prints the number of screens required to display a series of input values, where each input consists of two integers x and y. It reads the number of test cases (t) and then t lines of input, each containing x and y. For each input pair, it determines the total space required, calculates the number of screens needed to display y, and checks if there is enough remaining space to display x. If there is not enough space, it calculates the additional screens required to display x. The function then prints a list of n integers, where n is the number of test cases, and each integer represents the total number of screens required to display the corresponding input values of x and y.

