#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of three lines. The first line contains two integers n and m (1 <= n <= 2*10^5, 1 <= m <= 10^4). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^4). The third line contains a string s consisting of n characters 'L' and 'R'.
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
        
        y = [0] * n
        
        y[-1] = k
        
        for i in range(n - 2, -1, -1):
            if t[i] == 'R':
                k = k * a[q2] % m
                q2 += 1
            else:
                k = k * a[q1] % m
                q1 -= 1
            y[i] = k
        
        print(*y)
        
    #State: The output state after the loop executes all the iterations is a list of integers, where each integer is the result of a series of modular multiplications of the input integers a_i, based on the direction of the corresponding character in the string s. The direction of the characters in the string s determines whether to multiply the current result by the next or previous integer in the list a. The output list is in the reverse order of the input list a.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers (n and m), a list of n integers (a_1 to a_n), and a string of n characters ('L' and 'R'). It then performs a series of modular multiplications based on the direction of the characters in the string, either multiplying the current result by the next or previous integer in the list. The function outputs a list of integers, where each integer is the result of these modular multiplications, in the reverse order of the input list. The function repeats this process for each test case.

