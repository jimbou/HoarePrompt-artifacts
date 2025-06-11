#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two integers n and k (1 <= n, k <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (-10^9 <= a_i <= 10^9).
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
        
    #State: T is an integer equal to the number of test cases and must be at least 1, MOD is 1000000007, stdin contains 0 test cases, n is an integer between 1 and 2 * 10^5 inclusive, k is an integer and must be at least 1, a is a list of n integers, s is the sum of the integers in a, t is the maximum of tmp + x and the first integer in the list a and also the maximum of tmp and the previous value of t, _ is T-1, ans is ((s + t) % MOD + MOD) % MOD + 2 * t % MOD + t, i is 0, tmp is either 0 if tmp was originally negative, otherwise tmp is tmp + x, t is 2 times the previous value of t modulo MOD, ans is the previous value of ans plus 2 times the previous value of t modulo MOD, and the value of ans is printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains n integers. It calculates the sum of the integers, finds the maximum subarray sum, and then performs a series of calculations involving modular arithmetic to produce a final result, which is printed to the console. The function repeats this process for each test case.

