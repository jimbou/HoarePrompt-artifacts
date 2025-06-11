#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 100) and then t lines, each containing two space-separated integers x and y (0 <= x, y <= 9).
    x = int(input())
    for i in range(x):
        x, y = list(map(int, input().split()))
        
        if x > y:
            print(x, y)
        else:
            print(y, x)
        
    #State: The loop prints x lines, each containing two space-separated integers in descending order. The value of x is not changed.

#Overall this is what the function does:The function reads an integer t from standard input, followed by t lines of input, each containing two space-separated integers x and y. It then prints t lines of output, where each line contains the original x and y values in descending order. The function does not return any value and does not modify the original input values.

