#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of three lines. The first line contains two integers n and m (1 <= n <= 2*10^5, 1 <= m <= 10^4). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^4). The third line contains a string s of length n consisting of characters 'L' and 'R'.
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
        
    #State: stdin is empty, `ii` is `t`, `n`, `m`, `a`, `t`, `l`, `k`, `q1`, `q2`, `y`, `i` are undefined

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It reads an integer t, representing the number of test cases, followed by t test cases. Each test case consists of two integers n and m, n integers a_1 to a_n, and a string s of length n containing 'L' and 'R' characters. The function then performs calculations based on the input values and prints the result. After processing all test cases, the function leaves stdin empty and all variables used within the function are undefined.

