#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four inputs: first an integer t, then an integer n, then a list of n integers a_1, a_2, ..., a_n, then an integer m, and finally m pairs of integers x_i and y_i.
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
        
    #State: The output state after the loop executes all the iterations is a list of integers representing the cumulative sum of the differences between consecutive elements in the input list, followed by the string 'B'. The list is then used to calculate and print the sum of differences between specific pairs of elements in the list.

#Overall this is what the function does:This function processes multiple test cases from standard input. For each test case, it reads a list of integers and calculates the cumulative sum of differences between consecutive elements. It then uses this cumulative sum to calculate and print the sum of differences between specific pairs of elements in the list. The function iterates over all test cases, processing each one independently and printing the results for each pair of elements.

