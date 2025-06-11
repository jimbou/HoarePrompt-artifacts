#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains four space-separated integers: n, f, a, and b. The second line contains n space-separated integers.
    t = int(input(''))
    while t > 0:
        n, f, a, b = map(int, input('').split(' '))
        
        ls = [0] + list(map(int, input('').split(' ')))
        
        for i in range(1, n + 1):
            f = f - min(a * (ls[i] - ls[i - 1]), b)
        
        if f > 0:
            print('YES')
        else:
            print('NO')
        
        t -= 1
        
    #State: t is 0, and the stdin is empty.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains four integers: n, f, a, and b. The second line contains n integers. The function then calculates the value of f by subtracting the minimum of a times the difference between consecutive integers and b, for each pair of consecutive integers. If the final value of f is greater than 0, it prints 'YES', otherwise it prints 'NO'. The function repeats this process until all test cases have been processed, at which point the standard input is empty and the variable t is 0.

