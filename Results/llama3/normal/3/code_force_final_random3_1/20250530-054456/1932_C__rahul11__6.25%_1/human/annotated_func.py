#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of three lines. The first line contains two integers n and m (1 <= n <= 2*10^5, 1 <= m <= 10^4). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^4). The third line contains a string s consisting of n characters 'L' and 'R'.
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
        
    #State: MOD is 1000000006, n is an integer, m is an integer, arr is a list of n integers, s is a list of characters, res is a list of n integers, ans is 1, _ is t, stdin contains 0 test cases, i is the last element of arr, c is n, k is n - 1, l is n - 1, r is 0, and the list res is being printed

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the result. It accepts a series of test cases, each consisting of two integers (n and m) and a list of n integers, followed by a string of n characters ('L' and 'R'). The function calculates the product of the integers modulo m and MOD (1000000006), then iteratively updates this product based on the characters in the string, moving left or right through the list of integers. The final result is a list of n integers, which is printed to the console.

