#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing an integer x (2 <= x <= 1000).
    for i in range(int(input())):
        x = int(input())
        
        y = x - 1
        
        print(y)
        
    #State: The output state will be a series of integers, each being one less than the corresponding input integer. For example, if the input is 3, 4, 5, the output will be 2, 3, 4.

#Overall this is what the function does:The function reads a series of integers from standard input, subtracts 1 from each integer, and prints the resulting integers. It processes a number of integers specified by the first input value, which is expected to be between 1 and 1000. Each subsequent integer is expected to be between 2 and 1000. The function does not return any value but instead prints the modified integers to standard output.

