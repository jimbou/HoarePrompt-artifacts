#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t lines each containing a single integer n (2 <= n <= 10^3).
    for i in range(0, int(input())):
        n = int(input())
        
        print(1, 1)
        
        print(1, 2)
        
        for i in range(3, n + 1):
            print(i, i)
        
    #State: The output state will contain 2t lines. Each pair of lines will contain the numbers 1 and 1, followed by 1 and 2. The remaining lines will contain the numbers from 3 to n, where n is the input number, each paired with itself.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer t represents the number of test cases, and each subsequent integer n represents the number of lines to print for that test case. The function then prints 2t lines to standard output, with each pair of lines containing the numbers 1 and 1, followed by 1 and 2, and the remaining lines containing the numbers from 3 to n paired with themselves.

