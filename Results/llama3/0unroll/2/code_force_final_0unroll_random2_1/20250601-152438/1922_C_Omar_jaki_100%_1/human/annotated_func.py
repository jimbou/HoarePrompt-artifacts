#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four inputs: first an integer, then a list of unique non-decreasing integers, then an integer, and then a list of pairs of unique integers. The first integer is a positive integer. The list of integers is non-empty and contains unique non-decreasing integers. The second integer is a positive integer and is less than or equal to the length of the list of integers. The list of pairs of integers is non-empty and contains pairs of unique integers that are present in the list of integers.
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
        
    #State: t is 0, stdin contains no test cases, and the output contains the results of all the test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, each containing a list of unique non-decreasing integers and a list of pairs of unique integers. It then calculates and prints the results of all test cases, where each result is the difference between the cumulative sum of differences between consecutive integers in the list, up to the second integer in the pair, and the cumulative sum of differences up to the first integer in the pair. The function continues this process until all test cases have been processed, leaving the standard input empty and the output containing the results of all test cases.

