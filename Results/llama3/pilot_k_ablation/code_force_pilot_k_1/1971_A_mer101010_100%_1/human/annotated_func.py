#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two space-separated integers x and y (0 <= x, y <= 9).
    n = int(input())
    t = 0
    for i in range(n):
        a, b = map(int, input().split())
        
        if a < b:
            print(a, b)
        elif a == b:
            print(a, b)
        else:
            print(b, a)
        
    #State: `n` is an integer equal to t (1 <= n <= 100), t is 0, stdin is empty, `i` is equal to `n`, `a` and `b` are the last two integers read from stdin, for each pair of integers read from stdin, the smaller integer is printed first, followed by the larger integer.

#Overall this is what the function does:Reads a series of integer pairs from standard input, sorts each pair in ascending order, and prints the sorted pairs. The function does not return any value but modifies the standard output by printing the sorted integer pairs.

