#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two space-separated integers x and y (0 <= x, y <= 9).
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        print(max(a, b), min(a, b))
        
    #State: The output contains `t` lines, each containing two space-separated integers, where the first integer is the maximum of `x` and `y`, and the second integer is the minimum of `x` and `y`.

#Overall this is what the function does:The function reads a series of pairs of integers from standard input, determines the maximum and minimum values in each pair, and prints the maximum value followed by the minimum value for each pair, resulting in a sorted output of the input pairs.

