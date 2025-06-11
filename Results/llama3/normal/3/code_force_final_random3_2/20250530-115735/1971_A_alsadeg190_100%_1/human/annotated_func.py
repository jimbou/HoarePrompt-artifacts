#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two space-separated integers x and y (0 <= x, y <= 9).
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x < y:
            print(x, y)
        else:
            print(y, x)
        
    #State: `x` and `y` are integers between 0 and 9, `i` is `x-1`, stdin is empty. If `x` is less than `y`, the current values of `x` and `y` are printed. Otherwise, the value of `y` and the value of `x` (which is not less than `y`) are printed.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, where the first integer specifies the number of pairs to read. It then prints each pair in sorted order, with the smaller integer first. The function does not return any value, and its purpose is to output the sorted pairs to the console.

