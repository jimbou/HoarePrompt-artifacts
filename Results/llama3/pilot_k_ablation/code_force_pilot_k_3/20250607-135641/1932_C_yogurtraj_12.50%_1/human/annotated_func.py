#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of three lines: the first line contains two integers n and m (1 <= n <= 2*10^5, 1 <= m <= 10^4), the second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^4), and the third line contains a string s consisting of n characters 'L' and 'R'.
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
        
    #State: `ii` is equal to the initial value of `t`, `n` is an integer, `m` is an integer, `a` is a list of integers, `t` is a string, `l` is an integer, `y` is the string representation of `k` followed by a space and the string representation of `k` repeated `n-1` times, `k` is either the remainder of the product of the original value of `k` and the integer at index `q2` of list `a` divided by `m` or the remainder of the product of the original value of `k` and the integer at index `q1` of list `a` divided by `m`, `q2` is either `q2 + 1` or `q2`, `q1` is either `q1 - 1` or `q1`, `i` is -1, stdin contains 0 test cases, and the reverse of the string `y` is being printed.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output. It accepts an integer t, representing the number of test cases, followed by t test cases. Each test case consists of two integers n and m, a list of n integers a, and a string t of length n containing 'L' and 'R' characters. The function calculates a value k based on the input and prints the string representation of k followed by a space and the string representation of k repeated n-1 times in reverse order. The function performs this process for each test case and then terminates, leaving stdin empty.

