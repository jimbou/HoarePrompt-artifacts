#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of three lines: the first line contains two integers n and m (1 <= n <= 2*10^5, 1 <= m <= 10^4), the second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^4), and the third line contains a string s of length n consisting of characters 'L' and 'R'.
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
        
    #State: The output state will be a series of lines, each containing n integers representing the values of y for each test case. The values of y are calculated based on the input values of a, m, and t, and represent the result of the modular multiplication of the elements of a in the order specified by t, starting from the last element. The output state will have the same format as the initial state, with the addition of the calculated y values for each test case.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output to stdout. It accepts a series of test cases, each consisting of three lines: two integers n and m, a list of n integers a, and a string t of length n. The function calculates the modular multiplication of the elements of a in the order specified by t, starting from the last element, and prints the resulting values for each test case. The output is a series of lines, each containing n integers representing the calculated values.

