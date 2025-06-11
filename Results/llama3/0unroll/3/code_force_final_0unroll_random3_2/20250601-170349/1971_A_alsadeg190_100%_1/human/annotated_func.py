#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 100) and then t lines, each containing two space-separated integers x and y (0 <= x, y <= 9).
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x < y:
            print(x, y)
        else:
            print(y, x)
        
    #State: The loop prints x lines, each containing two space-separated integers, where the first integer is always less than or equal to the second integer. The value of x is not changed.

#Overall this is what the function does:The function reads a series of pairs of integers from standard input, sorts each pair in ascending order, and prints the sorted pairs. It takes no arguments and returns no value, only producing output to the console. The input pairs are processed independently, and the function does not modify the original input values.

