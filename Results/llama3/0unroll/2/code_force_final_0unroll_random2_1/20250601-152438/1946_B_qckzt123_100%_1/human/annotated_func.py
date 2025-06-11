#State of the program right berfore the function call: stdin contains several test cases. Each test case contains two lines. The first line contains two integers n and k (1 <= n, k <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (-10^9 <= a_i <= 10^9).
    MOD = 1000000007
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        n, k = map(int, sys.stdin.readline().strip().split())
        
        a = list(map(int, sys.stdin.readline().strip().split()))
        
        s = sum(a)
        
        t, tmp = 0, 0
        
        for x in a:
            tmp += x
            if tmp < 0:
                tmp = 0
            t = max(tmp, t)
        
        ans = ((s + t) % MOD + MOD) % MOD
        
        for i in range(k - 1):
            t *= 2
            t %= MOD
            ans += t
            ans %= MOD
        
        print(ans)
        
    #State: Output State: T is an integer equal to 0, MOD is 1000000007, stdin contains no test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains n integers. The function calculates a result for each test case by summing the integers, finding the maximum cumulative sum, and then performing a series of operations involving modular arithmetic. The final result for each test case is printed to the console. After processing all test cases, the function concludes, leaving the standard input empty.

