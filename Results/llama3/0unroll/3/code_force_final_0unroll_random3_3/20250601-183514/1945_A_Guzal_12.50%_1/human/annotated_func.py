#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three non-negative integers a, b, c, where a is the number of introverts, b is the number of extroverts, and c is the number of universals.
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        k = 0
        
        if (b % 3 != 0 and c < 3) and (b + c) % 3 != 0:
            print(-1)
        else:
            k += a + (b + c) // 3
            if (b + c) % 3 != 0:
                k += 1
            print(k)
        
    #State: The number of test cases `n` remains unchanged, but for each test case, the output will be the calculated value of `k`, which represents the total number of items that can be formed using the given values of `a`, `b`, and `c`. The value of `k` is calculated based on the conditions specified in the loop body. If the conditions are not met, the output will be -1.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three non-negative integers representing the number of introverts, extroverts, and universals. It then calculates and prints the total number of items that can be formed using these values, following specific conditions. If the conditions are not met, it prints -1. The function processes all test cases and outputs the calculated values or -1 for each case, without modifying the original input values.

