#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two space-separated non-negative integers x and y such that x != y. The number of test cases is specified in the first line of stdin.
    for i in range(int(input())):
        n, m = map(int, input().split())
        
        k = abs(n - m)
        
        if k & k - 1 == 0:
            print(k)
        elif n == 0 and m % 2 != 0:
            print(1)
        elif n == 0 and m % 2 == 0:
            print(2)
        else:
            l = bin(k).replace('0b', '')
            p = len(l)
            q = 2 ** (p - 1)
            print(k - q)
        
    #State: The output state will contain the results of the given operations for each test case, which are the absolute difference between the two input numbers, or a specific value based on the conditions specified in the loop body. The output will be a series of numbers, each representing the result of the operations for a single test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two space-separated non-negative integers x and y. It calculates the absolute difference between x and y, and then performs specific operations based on the conditions: if the difference is a power of 2, it prints the difference; if x is 0 and y is odd, it prints 1; if x is 0 and y is even, it prints 2; otherwise, it prints the difference minus the largest power of 2 that is less than or equal to the difference. The function outputs the results of these operations for each test case.

