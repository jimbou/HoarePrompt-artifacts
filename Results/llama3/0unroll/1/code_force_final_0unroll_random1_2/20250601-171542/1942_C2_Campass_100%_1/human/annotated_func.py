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
        
    #State: The output state is the number of operations required to make all elements in the array equal, which is calculated and printed for each test case.

#Overall this is what the function does:This function reads input from stdin, processes multiple test cases, and prints the minimum number of operations required to make all elements in an array equal. It accepts no parameters and returns no value, instead printing the result for each test case. The function takes as input the number of test cases, followed by the test cases themselves, each consisting of three integers (n, x, y) and a list of x distinct integers. It calculates the minimum number of operations required to make all elements in the array equal by sorting the list, calculating the differences between consecutive elements, and then processing these differences to determine the minimum number of operations. The result is printed for each test case.

