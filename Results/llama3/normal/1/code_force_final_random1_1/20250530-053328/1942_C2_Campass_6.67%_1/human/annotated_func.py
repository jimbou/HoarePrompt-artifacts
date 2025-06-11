#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of two lines. The first line contains three integers n, x, and y (4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), 0 <= y <= n - x). The second line contains x distinct integers from 1 to n.
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
            if c == 1:
                sx += 1
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
        
        cons = min(n - 2, cons)
        
        print(cons)
        
    #State: t is 0, n is an integer from the input, x is an integer from the input, y is an integer from the input minus the sum of half of each element in the list val, sx is the number of times the difference between consecutive elements in l is 1 plus the sum of each element in the list val, l is a sorted list of integers from the input with n + the first element of the original list appended to the end, val is a sorted list containing the differences between consecutive elements in l minus 1, where even numbers come first, cons is the minimum of n - 2 and x + sx - 2, stdin contains -1 test cases, and the value of cons is printed, where cons is the minimum of n - 2 and x + sx - 2.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers (n, x, y) and a list of x distinct integers. It calculates the minimum number of operations required to make the list consecutive, considering the given constraints (x, y), and prints this value for each test case. The function iterates through all test cases, processing each one independently, and outputs the result for each case.

