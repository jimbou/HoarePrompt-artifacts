#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 100) and then t lines each containing two space-separated integers x and y (0 <= x, y <= 9).
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x < y:
            print(x, y)
        else:
            print(y, x)
        
    #State: `x` and `y` are integers, `i` is `x-1`, stdin is empty. If `x` is less than `y`, the values of `x` and `y` are printed. Otherwise, the values of `y` and `x` are printed.

#Overall this is what the function does:The function reads a series of pairs of integers from standard input, where the number of pairs is specified by the first input. It then prints each pair in sorted order, with the smaller number first. The function does not return any value, but instead prints the sorted pairs directly to the console.

