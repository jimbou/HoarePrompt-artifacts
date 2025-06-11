#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer n (1 ≤ n ≤ 50). The second line contains n integers k_1,k_2,...,k_n (2 ≤ k_i ≤ 20).
    t = int(input())
    for T in range(t):
        def lcm(l):
            g = 1
            for i in range(len(l)):
                g = g * l[i] // gcd(g, l[i])
            return g
        
        bets = int(input())
        
        a = [int(x) for x in input().split()]
        
        prod = lcm(a)
        
        sumo = 0
        
        for i in range(bets):
            a[i] = prod // a[i]
            sumo += int(a[i])
        
        if sumo >= prod:
            print(-1)
        else:
            ans = ''
            for i in range(bets):
                ans += str(a[i]) + ' '
            print(ans)
        
    #State: The output state after the loop executes all the iterations is that the standard output contains the results of the least common multiple (LCM) calculations for each test case. For each test case, if the sum of the LCMs divided by each number is greater than or equal to the LCM of all numbers, the output is -1. Otherwise, the output is a string of numbers, each representing the LCM divided by the corresponding number, separated by spaces. The variable `t` remains unchanged, and the standard input is empty after reading all test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n integers. For each test case, it calculates the least common multiple (LCM) of the n integers, then divides the LCM by each integer and sums the results. If the sum is greater than or equal to the LCM, it outputs -1; otherwise, it outputs a string of the LCM divided by each integer, separated by spaces. The function processes all test cases and outputs the results to standard output, leaving the standard input empty.

