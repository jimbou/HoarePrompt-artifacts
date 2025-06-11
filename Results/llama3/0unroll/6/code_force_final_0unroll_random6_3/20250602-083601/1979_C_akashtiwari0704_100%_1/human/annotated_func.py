#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 50). The second line contains n integers k_1,k_2,...,k_n (2 ≤ k_i ≤ 20).
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
        
    #State: Output State: The output state after the loop executes all the iterations is that the standard output (stdout) contains the results of the loop's executions, which are either the string "-1" or a sequence of space-separated integers, depending on the input values. The variable `t` remains unchanged, still holding a positive integer value. The standard input (stdin) is empty, as all the test cases have been read and processed by the loop.

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing an integer n and a list of n integers. For each test case, it calculates the least common multiple (LCM) of the integers, then divides the LCM by each integer to produce a new list. If the sum of the new list is greater than or equal to the LCM, it prints -1; otherwise, it prints the new list of integers separated by spaces. The function processes all test cases and produces output for each case, leaving the standard input empty and the variable t unchanged.

