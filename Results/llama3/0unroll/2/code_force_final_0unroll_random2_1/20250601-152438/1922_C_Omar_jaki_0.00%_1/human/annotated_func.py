#State of the program right berfore the function call: stdin contains a series of test cases. Each test case contains: an integer t (1 <= t <= 10^4), an integer n (2 <= n <= 10^5), a list of n integers a_1, a_2, ..., a_n (0 <= a_1 < a_2 < ... < a_n <= 10^9), an integer m (1 <= m <= 10^5), and m lines each containing two integers x_i and y_i (1 <= x_i, y_i <= n; x_i != y_i).
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
        
        print(b, 'B')
        
        u, = r()
        
        while u:
            u -= 1
            c, d = r()
            if c < d:
                print(b[(d - 1) * 2] - b[(c - 1) * 2])
            else:
                print(b[c * 2 - 1] - b[d * 2 - 1])
        
    #State: t is 0, stdin is empty, r is the same lambda function

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case contains an integer t, an integer n, a list of n integers, an integer m, and m lines of two integers. It then calculates and prints the cumulative sum of the differences between consecutive elements in the list, and finally, it reads and processes m queries, printing the sum of the differences between the elements at the specified indices. The function continues this process until all test cases have been processed, at which point the standard input is empty.

