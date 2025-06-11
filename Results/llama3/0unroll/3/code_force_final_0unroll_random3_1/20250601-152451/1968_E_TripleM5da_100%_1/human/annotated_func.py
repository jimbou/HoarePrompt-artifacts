#State of the program right berfore the function call: stdin contains one input: a positive integer.
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: The output state is a series of print statements, where each iteration of the loop prints three lines: "1 1", "1 2", and "i i" for i ranging from 3 to the input number n. The number of iterations is equal to the initial input number. The stdin contains no more inputs after the loop finishes execution.

#Overall this is what the function does:This function reads a positive integer from standard input, then for each number from 1 to the input integer, it prints a series of three lines: "1 1", "1 2", and "i i" where i ranges from 3 to the current number. The function does not return any value, and its output is solely through print statements.

