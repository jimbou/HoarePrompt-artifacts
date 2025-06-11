#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4), then t test cases. Each test case contains two integers n and m (1 <= n <= 2*10^5, 1 <= m <= 10^4), then n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^4), then a string s consisting of n characters 'L' and 'R'.
    MOD = 10 ** 9 + 6
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        arr = list(map(int, input().split()))
        
        s = list(input())
        
        res = [0] * n
        
        ans = 1
        
        for i in arr:
            ans *= i
        
        res[0] = ans % m % MOD
        
        c = 1
        
        l = 0
        
        r = n - 1
        
        for k in range(n - 1):
            if s[k] == 'L':
                ans = ans // arr[l] % MOD
                res[c] = ans % m % MOD
                l += 1
            else:
                ans = ans // arr[r] % MOD
                res[c] = ans % m % MOD
                r -= 1
            c += 1
        
        print(*res)
        
    #State: The output state after the loop executes all the iterations is a list of integers, where each integer is the result of the modular exponentiation of the product of the elements in the array `arr` with the modulus `m` and `MOD`, after each iteration of the loop. The list is printed to the console. The values of `MOD`, `t`, `n`, `m`, `arr`, and `s` remain unchanged.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the results to the console. It accepts a series of test cases, each containing two integers (n and m) and a list of integers (arr) followed by a string (s). The function calculates the product of the elements in arr, performs modular exponentiation with m and MOD, and then iteratively updates the result based on the characters in s. The final state of the program is a list of integers representing the results of the modular exponentiation after each iteration, which is printed to the console.

