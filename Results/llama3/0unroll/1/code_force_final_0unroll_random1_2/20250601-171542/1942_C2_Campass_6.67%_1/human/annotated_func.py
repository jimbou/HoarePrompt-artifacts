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
        
    #State: The loop iterates t times, each time processing a test case. For each test case, it reads three integers n, x, and y from the input, and then reads a list of integers from the input. It sorts the list and calculates the number of consecutive integers that can be formed using the integers in the list, considering the constraints x and y. The result is printed for each test case. After all iterations, the loop terminates, and the output state is the collection of results printed for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers (n, x, y) and a list of x distinct integers. It calculates the maximum number of consecutive integers that can be formed using the integers in the list, considering the constraints x and y, and prints the result for each test case. The function iterates over the test cases, processing each one independently, and terminates after all test cases have been processed, leaving the output state as the collection of results printed for each test case.

