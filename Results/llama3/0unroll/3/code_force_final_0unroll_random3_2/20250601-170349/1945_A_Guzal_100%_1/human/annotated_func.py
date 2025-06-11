#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers a, b, c (0 <= a, b, c <= 10^9) — the number of introverts, extroverts, and universals, respectively.
    n = int(input())
    for i in range(n):
        a, b, c = map(int, input().split())
        
        k = 0
        
        if b % 3 != 0 and b % 3 + c < 3:
            print(-1)
        else:
            k += a + (b + c) // 3
            if (b + c) % 3 != 0:
                k += 1
            print(k)
        
    #State: Output State: The output state will be the number of groups that can be formed from the introverts, extroverts, and universals in each test case, or -1 if it is not possible to form groups. The number of groups will be the sum of the number of introverts and the total number of extroverts and universals divided by 3, rounded up to the nearest integer. If the total number of extroverts and universals is not a multiple of 3, 1 will be added to the total number of groups.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of three integers representing the number of introverts, extroverts, and universals. It then calculates the number of groups that can be formed from these individuals, where each group consists of three people. If it is not possible to form groups, it outputs -1. Otherwise, it outputs the total number of groups, which is the sum of the number of introverts and the total number of extroverts and universals divided by 3, rounded up to the nearest integer.

