#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three non-negative integers a, b, and c, where a is the number of introverts, b is the number of extroverts, and c is the number of universals.
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
        
    #State: n is 0, i is n, a, b, and c are integers, k is either 0 and -1 is printed if (b % 3 != 0 and c < 3) and (b + c) % 3 != 0. Otherwise, k is equal to its initial value plus a plus one-third of the sum of b and c. If the sum of b and c is not a multiple of 3, k is increased by 1, and the value of k is being printed.

#Overall this is what the function does:This function processes multiple test cases from standard input, each containing three non-negative integers representing the number of introverts, extroverts, and universals. For each test case, it calculates a value based on the number of introverts and the sum of extroverts and universals, taking into account whether the sum of extroverts and universals is a multiple of 3. If the sum of extroverts and universals is not a multiple of 3 and there are less than 3 universals, it prints -1. Otherwise, it prints the calculated value. The function continues this process until all test cases have been processed.

