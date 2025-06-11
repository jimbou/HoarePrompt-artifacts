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
        
    #State: The output state after the loop executes all the iterations is a list of integers, where each integer is the result of the modular exponentiation of the product of the elements in the array `arr` with the modulus `m` and `MOD`, and the result is printed for each test case. The state of the other variables in the precondition remains unchanged.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the results. It takes no parameters and returns no value. For each test case, it reads two integers (n and m), an array of n integers, and a string of n characters. It calculates the product of the array elements, performs modular exponentiation with modulus m and MOD, and prints the results for each test case. The function does not modify the input variables.

