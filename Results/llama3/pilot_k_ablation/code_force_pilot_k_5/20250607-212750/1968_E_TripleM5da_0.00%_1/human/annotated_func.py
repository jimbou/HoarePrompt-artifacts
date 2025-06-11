#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 50) and then t integers (2 <= n <= 10^3).
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 2):
            print(i, i)
        
    #State: Output State: `i` is `n + 2`, `n` is an integer, stdin contains some input, and the values 1, 2, and the values from 3 to `n + 2` (each twice) have been printed.
    #
    #In natural language, the output state after the loop executes all the iterations is that the loop variable `i` has reached the value of `n + 2`, where `n` is an integer. The input from stdin is still present, and the output includes the initial print statements (1, 1 and 1, 2), followed by the value of `i` being printed twice for each iteration of the loop, starting from 3 and ending at `n + 2`.

#Overall this is what the function does:The function reads a series of inputs from stdin, where the first input is an integer t (1 <= t <= 50) representing the number of test cases, followed by t integers n (2 <= n <= 10^3). For each test case, it prints a sequence of numbers, starting with (1, 1) and (1, 2), and then for each integer i from 3 to n + 2, it prints (i, i). The function does not return any value, and its purpose is to generate and print a specific pattern of numbers based on the input values.

