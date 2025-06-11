#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1000) and then t lines each containing an integer x (2 <= x <= 1000).
    for i in range(int(input())):
        x = int(input())
        
        y = x // 2
        
        print(y)
        
    #State: The output state will contain t lines, each containing the integer division of the corresponding input integer x by 2.

#Overall this is what the function does:The function reads a series of integers from standard input, performs integer division by 2 on each number, and prints the results to standard output. It takes no arguments and returns no value, modifying only the output state.

