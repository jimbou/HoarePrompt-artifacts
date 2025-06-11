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
        
    #State: The output state after the loop executes all the iterations is the number of operations required to make all elements in the list equal to the median of the list, which is the sum of the number of elements in the list and the sum of the differences between each element and the median, minus 2.

#Overall this is what the function does:This function calculates the minimum number of operations required to make all elements in a list equal to the median of the list. It reads input from stdin, processes multiple test cases, and outputs the result for each case. The function takes no parameters and returns the number of operations required, which is the sum of the number of elements in the list and the sum of the differences between each element and the median, minus 2.

