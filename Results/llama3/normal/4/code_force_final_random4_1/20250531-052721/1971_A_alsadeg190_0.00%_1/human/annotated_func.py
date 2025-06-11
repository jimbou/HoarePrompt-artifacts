#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two space-separated integers x and y (0 <= x, y <= 9).
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x > y:
            print(x, y)
        else:
            print(y, x)
        
    #State: `i` is `x`, stdin is empty, and all pairs of integers from the input have been printed in the order that makes `x` greater than or equal to `y`.

#Overall this is what the function does:This function reads a specified number of pairs of integers from standard input, sorts each pair in non-decreasing order, and prints the sorted pairs. It consumes all input and leaves the input stream empty.

