#State of the program right berfore the function call: stdin contains one input: an integer (greater than or equal to 1 and less than or equal to 50) representing the number of test cases, followed by that many integers (greater than or equal to 2 and less than or equal to 10^3).
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 2):
            print(i, i)
        
    #State: stdin is empty, `i` is the number of test cases (between 1 and 50 inclusive), `n` is the last integer input (between 2 and 10^3 inclusive), and the numbers 1 and 2 are printed twice for each test case, and numbers from 3 to `n + 1` are printed twice for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer between 2 and 10^3. For each test case, it prints a sequence of numbers, starting with 1 and 2, and then printing each number from 3 to the input number plus one, twice. The function processes between 1 and 50 test cases, as specified by the first input integer, and leaves the standard input empty after execution.

