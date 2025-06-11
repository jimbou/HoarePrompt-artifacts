#State of the program right berfore the function call: **stdin contains a series of test cases. Each test case consists of four parts:
    r = lambda : map(int, input().split())
    t, = r()
    while t:
        t -= 1
        
        r()
        
        a = -1000000000.0, *r(), 2000000000.0
        
        b = [0, 0]
        
        for w, x, y, z in zip(a, a[1:], a[2:], a[3:]):
            v = y - x
            b += b[-2] + v ** (v > x - w), b[-1] + v ** (v > z - y)
        
        u, = r()
        
        while u:
            u -= 1
            c, d = r()
            if c < d:
                print(b[(d - 1) * 2] - b[(c - 1) * 2])
            else:
                print(b[c * 2 - 1] - b[d * 2 - 1])
        
    #State: t = 0, b = [0, 0], u = 0

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of four parts. It processes the input data, performs calculations, and stores the results in an array. Then, it reads a number of queries, and for each query, it prints the difference between two values in the array, depending on the query parameters. The function repeats this process until all test cases have been processed.

