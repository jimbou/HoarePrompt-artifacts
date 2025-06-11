#State of the program right berfore the function call: stdin contains two inputs: first an integer (greater than 0) and then a series of integers (greater than 1) equal to the first integer.
    t = int(input())
    for i in range(t):
        n = int(input())
        
        print('1 1')
        
        print('1 2')
        
        if n == 3:
            print('2 3')
        elif n >= 4:
            print('2 4')
            for j in range(4, n + 1):
                print(str(j) + ' ' + str(j))
        
    #State: `t` is 0, `i` is `t`, `n` is an integer, stdin is empty, '1 1' and '1 2' are printed `t` times. If `n` equals 3, '2 3' is printed. If `n` is not equal to 3, and `n` is greater than or equal to 4, '2 4' is printed, and 'j j' is printed for all j from 4 to n, for each iteration of the loop.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer represents the number of test cases, and each subsequent integer represents the number of operations to perform. For each test case, it prints a series of pairs of integers, starting with '1 1' and '1 2', and then either '2 3' if the number of operations is 3, or '2 4' followed by pairs of identical integers from 4 to the number of operations if the number of operations is 4 or more. The function consumes all input from standard input and produces output in the form of these pairs of integers.

