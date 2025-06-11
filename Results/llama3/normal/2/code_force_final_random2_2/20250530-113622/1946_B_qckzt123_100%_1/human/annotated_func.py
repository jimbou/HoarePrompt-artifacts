#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains two integers n and k (1 <= n, k <= 2 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (-10^9 <= a_i <= 10^9). The sum of the values of n and k for all test cases does not exceed 2 * 10^5.
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
        
    #State: T is an integer representing the number of test cases that must be greater than or equal to 0, _ is T, n is an integer, k is an integer that must be at least 1, a is a list of integers, s is the sum of the integers in a, t is the maximum subarray sum of a multiplied by 2 to the power of k-1 and then taken modulo MOD, tmp is 0 if the maximum subarray sum of a is negative, otherwise tmp is the maximum subarray sum of a, ans is the remainder of the sum of s, t multiplied by 2 to the power of k-1 and then taken modulo MOD, i is k-1, and stdin contains 0 test cases, and the value of ans which is the remainder of the sum of s, t multiplied by 2 to the power of k-1 and then taken modulo MOD is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains two integers n and k, and the second line contains n integers. The function calculates the sum of the integers, the maximum subarray sum, and then combines these values using a specific formula involving modular arithmetic. The result is printed for each test case. The function processes all test cases and then terminates, leaving the standard input empty.

