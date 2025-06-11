#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two space-separated integers x and y (0 <= x, y <= 9).
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        print(max(a, b), min(a, b))
        
    #State: t is an integer between 1 and 100 (inclusive), _ is t-1, a and b are integers between 0 and 9, stdin contains 0 lines, and the maximum and minimum values between a and b are being printed.

#Overall this is what the function does:Reads a series of pairs of integers from standard input, where the number of pairs is specified by an initial integer, and prints each pair with the maximum value first and the minimum value second.

