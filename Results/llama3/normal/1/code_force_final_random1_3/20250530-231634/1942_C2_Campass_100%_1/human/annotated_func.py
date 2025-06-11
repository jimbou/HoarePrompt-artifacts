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
        
    #State: t is equal to 0, n is an integer between 4 and 10^9, x is an integer between 2 and min(n, 2 * 10^5), sx is equal to the sum of all elements in val, y is an integer between 0 and n - x minus the sum of all c values, l is a sorted list of x distinct integers from 1 to n with n + the first element of l appended to the end, val is an empty list, i is equal to the last element of val, c is equal to i // 2, cons is equal to x + sx - 2, stdin contains 0 test cases, and cons is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers (n, x, y) and a list of x distinct integers. It calculates the minimum number of operations required to make all integers in the list consecutive, considering the constraints x and y, and prints this value for each test case. The function processes all test cases and then terminates, leaving the input stream empty.

