#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4), followed by t test cases. Each test case consists of three lines: the first line contains two integers n and m (1 <= n <= 2*10^5, 1 <= m <= 10^4), the second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^4), and the third line contains a string s of length n consisting of characters 'L' and 'R'.
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
        
    #State: Output State: The loop has executed all the iterations, and the output state is as follows: The value of `MOD` remains unchanged at 1000000006. The value of `t` has been consumed and is no longer available. The loop has processed all `t` test cases, and for each test case, it has calculated and printed the `res` array. The `res` array contains the result of the calculation for each test case, which is the product of the elements in the `arr` array, taken modulo `m` and then modulo `MOD`, for each position in the array. The `ans` variable has been updated and used to calculate the `res` array for each test case. The `c`, `l`, and `r` variables have been used to keep track of the current position in the `arr` and `s` arrays, and have been updated accordingly. The `s` array has been consumed and is no longer available. The `arr` array has been consumed and is no longer available. The `n` and `m` variables have been consumed and are no longer available. The `res` array has been printed for each test case.

#Overall this is what the function does:This function reads input from standard input, processes multiple test cases, and prints the results. It takes no arguments and returns no value. For each test case, it reads two integers (n and m) and an array of n integers, followed by a string of n characters ('L' or 'R'). It calculates the product of the array elements modulo m and MOD (10^9 + 6), and then updates the product by removing elements from the left or right based on the characters in the string. The final product values are stored in an array and printed for each test case.

