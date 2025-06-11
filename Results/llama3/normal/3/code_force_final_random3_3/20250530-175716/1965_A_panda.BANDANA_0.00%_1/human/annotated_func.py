#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4), followed by t test cases. Each test case contains an integer n (1 <= n <= 2*10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: t is an integer between 1 and 10^4 (inclusive), i is t-1, n is an integer, l is a list of integers, e is a set of integers, m is an integer equal to the length of l, stdin contains 0 test cases. If 1 is in the list l, then 'Bob' is printed. Otherwise, 'Alice' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case contains a list of integers. It then determines whether the number 1 is present in the list and prints 'Bob' if it is, or 'Alice' if it is not. The function processes multiple test cases and provides a separate output for each case.

