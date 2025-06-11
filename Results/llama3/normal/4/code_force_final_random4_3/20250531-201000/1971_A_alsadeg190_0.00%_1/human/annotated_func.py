#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two space-separated integers x and y (0 <= x, y <= 9).
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x > y:
            print(x, y)
        else:
            print(y, x)
        
    #State: `x` and `y` are integers between 0 and 9 inclusive, `i` is `x-1`, stdin contains 0 lines. If `x` is greater than `y`, the values of `x` and `y` are printed. Otherwise, the values of `y` and `x` are printed.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, compares each pair, and prints the pair in the order where the larger number comes first. The function processes a variable number of pairs, as specified by the first integer read from standard input.

