#State of the program right berfore the function call: stdin contains an integer t, followed by t test cases. Each test case consists of two lines. The first line contains three integers n, x, and y. The second line contains x distinct integers from 1 to n. The constraints are 1 <= t <= 10^4, 4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), and 0 <= y <= n - x.
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
        
    #State: The output state is a list of integers, where each integer represents the minimum number of operations required to make the array consecutive, for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers (n, x, y) and a list of x distinct integers. It calculates and prints the minimum number of operations required to make the array consecutive, considering the constraints provided. The function iterates through each test case, processes the input data, and outputs the minimum number of operations required for each case.

