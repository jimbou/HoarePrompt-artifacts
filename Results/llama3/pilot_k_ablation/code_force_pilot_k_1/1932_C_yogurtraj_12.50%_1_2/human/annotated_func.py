#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4), followed by t test cases. Each test case consists of three lines: the first line contains two integers n and m (1 <= n <= 2*10^5, 1 <= m <= 10^4), the second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^4), and the third line contains a string s of length n consisting of characters 'L' and 'R'.
    for ii in range(int(input())):
        n, m = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        t = input()
        
        l = t.count('L')
        
        k = 0
        
        q1 = 0
        
        q2 = 0
        
        if t[-1] == 'L':
            k = a[l - 1] % m
            q1 = l - 2
            q2 = l
        else:
            k = a[l] % m
            q1 = l - 1
            q2 = l + 1
        
        y = str(k)
        
        for i in range(n - 2, -1, -1):
            if t[i] == 'R':
                k = k * a[q2] % m
                q2 += 1
            else:
                k = k * a[q1] % m
                q1 -= 1
            y += ' ' + str(k)
        
        print(y[::-1])
        
    #State: `ii` is equal to the initial value of `t`, `n`, `m`, `a`, `t`, `l`, `k`, `q1`, `q2`, `y`, and `i` are no longer defined, `stdin` is empty, and the string representation of the remainders of the product of the elements of `a` corresponding to the 'R' and 'L' characters in `t` (in reverse order) divided by `m` for all test cases have been printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers (n and m), a list of n integers, and a string of n characters ('L' and 'R'). It then calculates the remainders of the product of the elements of the list corresponding to the 'R' and 'L' characters in the string, divided by m, in reverse order. The function prints the string representation of these remainders for each test case. After processing all test cases, the function leaves the input stream empty and all variables used within the function are no longer defined.

