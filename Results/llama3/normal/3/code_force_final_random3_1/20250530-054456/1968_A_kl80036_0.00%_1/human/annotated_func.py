#State of the program right berfore the function call: stdin contains t+1 inputs: the first input is an integer t (1 <= t <= 1000), and the remaining t inputs are integers x (2 <= x <= 1000).
    for i in range(int(input())):
        x = int(input())
        
        y = x // 2
        
        print(y)
        
    #State: i is t-1, stdin contains 0 inputs: integers, x is an integer equal to the last input integer, y is an integer equal to half of the last input integer, and the value of y which is half of the last input integer is being printed

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer t represents the number of subsequent integers to read. It then calculates and prints the integer division of each subsequent integer by 2. After processing all inputs, the function concludes, leaving the input stream empty.

