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
        
    #State: t is 0, n is an integer, x is an integer greater than 0, y is an integer equal to its original value minus the sum of all elements in val divided by 2, sx is an integer greater than or equal to 0 and equal to its original value plus the sum of all elements in val, l is a sorted list of x distinct integers from 1 to n, followed by n plus the first integer in the list, val is an empty list, cons is an integer equal to the minimum of n - 2 and x + sx - 2, and stdin contains 0 test cases.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers (n, x, y) and a list of x distinct integers from 1 to n. It calculates the minimum number of operations required to make the list consecutive, considering the given constraints (x, y), and prints the result for each test case. The function iterates through all test cases, modifying the input list and variables accordingly, until all test cases have been processed.

