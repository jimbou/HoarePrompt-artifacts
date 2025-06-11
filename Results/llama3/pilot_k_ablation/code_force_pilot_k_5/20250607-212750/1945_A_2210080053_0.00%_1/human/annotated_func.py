#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three non-negative integers (a, b, c) separated by a space, where a is the number of introverts, b is the number of extroverts, and c is the number of universals.
    for line in [*open(0)][1:]:
        p, q, r = map(int, line.split())
        
        q += r
        
        print((p - q // 3, -1)[r < q % 3])
        
    #State: p is an integer, q is an integer equal to its original value plus the number of test cases times r, r is an integer, the file object has at least 1 line, and this is printed: (p - q // 3, -1)[r < q % 3]

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains three non-negative integers representing the number of introverts, extroverts, and universals. It then calculates the total number of extroverts and universals, and prints the difference between the number of introverts and the total number of extroverts and universals divided by 3, unless the number of universals is less than the remainder of the total number of extroverts and universals divided by 3, in which case it prints -1.

