#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 100) and then t lines, each containing two space-separated integers x and y (0 <= x, y <= 9).
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x > y:
            print(x, y)
        else:
            print(y, x)
        
    #State: `x` and `y` are integers, `i` is `x-1`, stdin contains no input. The values of `x` and `y` are being printed, with `x` first if `x` is greater than `y`, otherwise `y` is printed first.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, compares each pair, and prints them in order, with the larger number first. It repeats this process for a number of iterations specified by the first input, which is also an integer.

