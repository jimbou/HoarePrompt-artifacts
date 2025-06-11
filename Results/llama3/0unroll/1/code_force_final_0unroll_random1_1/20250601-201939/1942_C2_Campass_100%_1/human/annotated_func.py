#State of the program right berfore the function call: stdin contains an integer t, followed by t test cases. Each test case consists of two lines. The first line contains three integers n, x, and y. The second line contains x distinct integers from 1 to n. The input satisfies the following constraints: 1 <= t <= 10^4, 4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), 0 <= y <= n - x.
    R = lambda : map(int, input().split())
    t, = R()
    while t:
        t -= 1
        
        n, x, y = R()
        
        sx = 0
        
        l = list(R())
        
        l.sort()
        
        l.append(n + l[0])
        
        val = []
        
        for i in range(1, x + 1):
            c = l[i] - l[i - 1] - 1
            val.append(c)
        
        val.sort(key=lambda x: (1 - x & 1, x))
        
        for i in val:
            c = i // 2
            if y < c:
                sx += y * 2
                break
            sx += i
            y -= c
        
        cons = x + sx - 2
        
        print(cons)
        
    #State: The value of t is 0, and the values of n, x, y, sx, l, and val are updated according to the last test case. The value of cons is printed for each test case.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of three integers (n, x, y) and a list of x distinct integers. It then calculates the minimum number of operations required to make all integers in the list consecutive, considering the constraints x and y, and prints this value for each test case. The function iterates through all test cases and updates its internal state accordingly, ultimately printing the result for each case.

