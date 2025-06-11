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
        
    #State: MOD is 1000000006, stdin contains 0 inputs, n is an integer at least 1 and at most 2*10^5, m is an integer between 1 and 10^4, arr is an empty list, s is a list of n characters 'L' and 'R', res is a list of n integers with the first element equal to ans % m % MOD and the rest are zeros except for the third element which is equal to ans % m % MOD and the fifth element which is equal to ans % m % MOD and so on until the last element which is equal to ans % m % MOD, ans is equal to the product of all integers in the list divided by the first element of arr if s[k] is 'L', otherwise divided by arr[r] % MOD, _ is the number of test cases, i is the last integer in the list, c is n, l is n if s[k] is 'L', otherwise 0, r is 0 if s[k] is 'L', otherwise n - 1, k is n - 1, and the following is printed: the list res containing the first element equal to ans % m % MOD and the rest are zeros except for the third element which is equal to ans % m % MOD and the fifth element which is equal to ans % m % MOD and so on until the last element which is equal to ans % m % MOD.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the result. It accepts a number of test cases, and for each test case, it reads two integers (n and m) and a list of n integers, followed by a string of n characters ('L' and 'R'). It calculates the product of the integers modulo m and MOD (1000000006), and then iterates through the string, updating the product by dividing it by the corresponding integer in the list based on the character in the string ('L' or 'R'). The function prints the resulting list of products modulo m and MOD.

