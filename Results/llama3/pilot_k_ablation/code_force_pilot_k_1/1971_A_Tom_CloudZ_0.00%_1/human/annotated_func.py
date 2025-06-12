#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two space-separated integers x and y (0 <= x, y <= 9).
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        print(max(a, b), min(a, b))
        
    #State: `t` is an integer between 1 and 100 (inclusive), stdin is empty, and the maximum and minimum values between each pair of `x` and `y` have been printed.

#Overall this is what the function does:This function reads a series of pairs of integers from standard input, determines the maximum and minimum value in each pair, and prints them in that order. It continues this process until all input pairs have been processed, at which point the standard input is empty.

