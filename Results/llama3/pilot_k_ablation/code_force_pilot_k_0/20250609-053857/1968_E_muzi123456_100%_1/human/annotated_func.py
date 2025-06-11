#State of the program right berfore the function call: stdin contains one input: an integer (t) followed by t integers (n), where 1 <= t <= 50 and 2 <= n <= 10^3.
    t = int(input())
    while t:
        t -= 1
        
        n = int(input())
        
        print(n, end=' ')
        
        print(n)
        
        print(n, end=' ')
        
        print(n - 1)
        
        if n == 3:
            print(2, end=' ')
            print(1)
        else:
            for i in range(1, n - 1):
                print(i, end=' ')
                print(i)
        
        print(' ')
        
    #State: The output state is a sequence of numbers printed to the console, where each number is repeated twice, followed by a space, and the sequence is repeated for each input number n. If n is 3, the sequence is 3 3 2 2 1 1, otherwise, it is n n n-1 n-1 ... 2 2 1 1.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer (t) specifies the number of subsequent integers (n) to process. For each n, it prints a sequence of numbers to the console, repeating each number twice, starting from n and decrementing to 1. If n is 3, the sequence is 3 3 2 2 1 1; otherwise, it follows the pattern n n n-1 n-1 ... 2 2 1 1. The function processes all input numbers specified by t, printing the sequences for each n.

