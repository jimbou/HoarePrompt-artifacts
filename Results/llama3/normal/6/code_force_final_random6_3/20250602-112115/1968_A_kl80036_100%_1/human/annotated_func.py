#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 ≤ t ≤ 1000) and then t lines each containing a single integer x (2 ≤ x ≤ 1000).
    for i in range(int(input())):
        x = int(input())
        
        y = x - 1
        
        print(y)
        
    #State: x is an integer equal to the last integer value from the original stdin, y is an integer equal to x - 1, i is t - 1, stdin contains no integer values, and y which is equal to x - 1 is being printed.

#Overall this is what the function does:The function reads a series of integers from standard input, subtracts 1 from each integer, and prints the resulting values. It processes a specified number of integers (t) provided at the beginning of the input, and after processing all integers, the standard input is exhausted. The function does not return any value but prints the decremented integers.

