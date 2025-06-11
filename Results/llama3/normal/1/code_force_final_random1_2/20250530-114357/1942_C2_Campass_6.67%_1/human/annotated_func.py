#State of the program right berfore the function call: stdin contains an integer t, followed by t test cases. Each test case consists of two lines. The first line contains three integers n, x, and y. The second line contains x distinct integers from 1 to n. 1 <= t <= 10^4, 4 <= n <= 10^9, 2 <= x <= min(n, 2 * 10^5), 0 <= y <= n - x.
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
        
    #State: t is 0, stdin contains 0 inputs, n is an integer, x is at least 1, y is y - sum of all integer divisions of all elements in val by 2, l is a sorted list of x distinct integers from 1 to n with n + the first element of the list appended to the end, val is a sorted list containing x elements which are l[1] - l[0] - 1, l[2] - l[1] - 1, ..., l[x] - l[x - 1] - 1, i is the last element in the list, sx is the number of times c is 1 plus 2 times y if y is less than c, otherwise sx is the number of times c is 1 plus the sum of all elements in val, c is the integer division of the last element in the list by 2, and the minimum of n - 2 and x + sx - 2 is printed, val is a list that must have at least x elements, and the minimum of n - 2 and x + sx - 2 is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers (n, x, y) and a list of x distinct integers from 1 to n. It then calculates the minimum number of consecutive integers that can be formed using the given integers and the additional integer y, and prints this minimum number for each test case. The function continues to process test cases until the input is exhausted.

