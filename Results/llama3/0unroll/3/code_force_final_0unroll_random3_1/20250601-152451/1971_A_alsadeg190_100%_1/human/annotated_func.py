#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two space-separated integers x and y (0 <= x, y <= 9).
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x < y:
            print(x, y)
        else:
            print(y, x)
        
    #State: The value of `x` is 1, and the stdin contains no lines. The loop has printed `t-1` lines, each containing two space-separated integers, where the first integer is less than or equal to the second integer.

#Overall this is what the function does:Reads a series of pairs of integers from standard input, sorts each pair in ascending order, and prints the sorted pairs. The function does not return any value, but instead prints the sorted pairs directly to the console.

