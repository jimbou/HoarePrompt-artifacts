#State of the program right berfore the function call: stdin contains several test cases. Each test case contains two lines. The first line contains two integers n and k (1 ≤ n, k ≤ 2 × 10^5). The second line contains n integers a_1, a_2, …, a_n (-10^9 ≤ a_i ≤ 10^9).
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
        
    #State: T is an integer greater than or equal to 0, MOD is 1000000007, stdin contains 0 test cases, n is an integer between 1 and 200000 inclusive, k is an integer at least 1, a is a list of n integers, x is the last integer in the list, s is the sum of the integers in a, _ is T-1, tmp is the maximum subarray sum of a, t is the maximum of tmp and the maximum of x and the maximum of 0 and the sum of the last integer in the list and its previous value and x, ans is (((s + t) % MOD + MOD) % MOD + (2 * t) % MOD + t) % MOD + ... + (2^(k-1) * t) % MOD, i is k-1, and ans is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing two lines. The first line contains two integers n and k, and the second line contains n integers. For each test case, it calculates the sum of the integers, the maximum subarray sum, and then computes a result by adding the sum and the maximum subarray sum, and then repeatedly adding twice the maximum subarray sum, modulo 1000000007, k-1 times. The final result is printed to standard output.

