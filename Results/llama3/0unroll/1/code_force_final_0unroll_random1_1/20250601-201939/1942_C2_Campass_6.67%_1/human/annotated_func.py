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
        
    #State: The final output state is the minimum number of operations required to make the array consecutive, which is the minimum of n-2 and the sum of x, sx, and -2.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and outputs the minimum number of operations required to make an array consecutive. It accepts no parameters and returns the minimum number of operations for each test case. The function's purpose is to calculate the minimum operations needed to make an array consecutive by analyzing the given array and the number of operations already performed. The final state of the program is the output of the minimum number of operations required for each test case, which is the minimum of n-2 and the sum of x, sx, and -2.

