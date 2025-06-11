#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two inputs: first an integer n and then a space-separated list of n integers. t is a positive integer, n is a positive integer, and the integers in the list are positive integers.
    t = int(input())
    for i in range(t):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        e = set(l)
        
        m = len(l)
        
        if 1 in l:
            print('Bob')
        else:
            print('Alice')
        
    #State: t is a positive integer greater than or equal to 0, i is t-1, n is a positive integer, l is a list of n positive integers, e is a set of n positive integers, m is equal to n, stdin contains 0 test cases. If 1 is in the list l, 'Bob' is printed. Otherwise, 'Alice' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a positive integer n followed by a list of n positive integers. It then checks if the number 1 is present in the list. If 1 is found, it prints 'Bob'; otherwise, it prints 'Alice'. The function processes all test cases and prints the corresponding result for each case.

