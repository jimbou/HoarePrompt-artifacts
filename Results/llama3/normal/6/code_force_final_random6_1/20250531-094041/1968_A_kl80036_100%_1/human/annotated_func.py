#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a series of integers (each representing a test case). The number of test cases is between 1 and 1000 inclusive. Each test case is an integer between 2 and 1000 inclusive.
    for i in range(int(input())):
        x = int(input())
        
        y = x - 1
        
        print(y)
        
    #State: x is an integer between 1 and 1000 inclusive, y is an integer between -999 and 999 inclusive, stdin is empty, i is equal to the number of test cases, and y which is an integer between -999 and 999 inclusive is being printed

#Overall this is what the function does:Reads a series of test cases from standard input, where each test case is an integer between 2 and 1000, and prints the result of subtracting 1 from each test case. The function processes between 1 and 1000 test cases, and after execution, the standard input is empty, and the results are printed to the console.

