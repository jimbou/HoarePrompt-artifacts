#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 100) and then t lines each containing two space-separated integers x and y (0 <= x, y <= 9).
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        print(min(a, b), max(a, b))
        
    #State: t is an integer between 1 and 100, a is an integer between 0 and 9, b is an integer between 0 and 9, _ is t-1, stdin is empty, and the minimum and maximum values of a and b are being printed, where the minimum value is the smaller of a and b, and the maximum value is the larger of a and b.

#Overall this is what the function does:The function reads a series of pairs of integers from standard input, where the number of pairs is specified by an initial integer input, and prints the minimum and maximum values of each pair.

