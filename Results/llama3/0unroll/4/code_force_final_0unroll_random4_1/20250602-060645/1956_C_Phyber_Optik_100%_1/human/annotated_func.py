#State of the program right berfore the function call: stdin contains one or more inputs: an integer (greater than 0) followed by one or more integers (greater than 0).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        sum = 1
        
        for i in range(2, n + 1):
            sum += (i * i - (i - 1) * (i - 1)) * i
        
        print(sum, n + n)
        
        for j in range(1, n + 1):
            print(1, n - j + 1, *range(1, n + 1))
            print(2, n - j + 1, *range(1, n + 1))
        
    #State: The loop has executed t iterations, and for each iteration, it has read an integer n from stdin, calculated a sum using a nested loop, printed the sum and 2n, and then printed 2n lines of output, each containing n+2 integers. The final state of the loop variables is: t is unchanged, n is the last integer read from stdin, sum is the last calculated sum, i is n, and j is n. The stdin stream has been consumed by t integers.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer represents the number of test cases, and each subsequent integer represents the size of a sequence. For each sequence, it calculates a sum using a nested loop, prints the sum and twice the sequence size, and then prints a series of lines, each containing a specific pattern of integers. The function consumes the input stream and produces output based on the calculated sums and sequence sizes.

