#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two space-separated integers x and y (0 <= x, y <= 9).
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x < y:
            print(x, y)
        else:
            print(y, x)
        
    #State: `x` is an integer between 1 and 100 (inclusive), stdin contains t - x lines, each containing two space-separated integers x and y (0 <= x, y <= 9). The values of `x` and `y` are printed in ascending order for each iteration of the loop.

#Overall this is what the function does:Reads a series of pairs of integers from standard input, where the number of pairs is specified by the first integer read, and prints each pair in ascending order.

