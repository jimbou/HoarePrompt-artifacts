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
        
    #State: n is an integer that must be at least 2, m is an integer, arr is a list of integers, s is a list of characters, res is a list of n integers where the first element is the product of all integers in arr modulo m modulo MOD, c is n, MOD is 1000000006, _ is t, stdin is empty, l is n - 1 if the number of 'L's in s is equal to n - 1, otherwise l is n - 1 - (the number of 'L's in s), r is 0 if the number of 'L's in s is equal to 0, otherwise r is the number of 'L's in s, k is n - 1, t is at least 1, i is the last integer in the list arr, and ans is the product of all integers in arr divided by the product of all integers at indices l and r in arr modulo MOD, and the list res is printed, where the first element of res is the product of all integers in arr modulo m modulo MOD, and the rest of the elements in res are not explicitly defined in the precondition

#Overall this is what the function does:This function reads input from stdin, processes it, and prints the result. It accepts a series of test cases, each consisting of two integers (n and m), a list of n integers, and a string of n characters ('L' or 'R'). The function calculates the product of the integers modulo m modulo MOD, then iteratively updates this product by dividing it by the integers at specific indices based on the characters in the string. The updated products are stored in a list, which is then printed. The function repeats this process for each test case until stdin is empty.

