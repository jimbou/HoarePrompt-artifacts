#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains three integers: n, x, and y (4 <= n <= 10^9, 2 <= x <= min(n, 2*10^5), 0 <= y <= n - x). The second line contains x distinct integers from 1 to n.
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
        
    #State: t is 0, n is an integer between 4 and 10^9 inclusive, x is an integer between 2 and min(n, 2*10^5) inclusive, sx is the sum of all elements in val if y is greater than or equal to all c's, otherwise sx is the sum of all elements in val plus 2*y times the number of times y is less than c, y is 0, l is a sorted list of x distinct integers from 1 to n, and l's last element is n plus the first element of l, val is an empty list, i is the last element of val, c is equal to i divided by 2, and cons is equal to x plus sx minus 2, and cons is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two lines. The first line contains three integers: n, x, and y, representing the total number of elements, the number of distinct integers, and a threshold value, respectively. The second line contains x distinct integers from 1 to n. The function then calculates the sum of the differences between consecutive integers in the sorted list, considering the threshold value y. If y is less than half of any difference, it adds 2*y to the sum. Finally, the function prints the result, which is the sum of the differences plus x minus 2, for each test case.

