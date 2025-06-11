#State of the program right berfore the function call: stdin contains a series of test cases. Each test case contains an integer n, followed by a list of n integers, followed by an integer q, followed by q pairs of integers.
    R = lambda : map(int, input().split())
    t, = R()
    while t:
        t -= 1
        
        R()
        
        a = [0]
        
        p = i = j = 0
        
        for x in R():
            j = (j, i)[x != p]
            a += j,
            p = x
            i += 1
        
        q, = R()
        
        while q:
            q -= 1
            l, r = R()
            print(*((a[r], r), [-1] * 2)[a[r] < l])
        
    #State: t is 0, a is [0, j, j, ..., j] with the original value of t elements, p is the last element in R, i is the original value of t, j is either its original value or equal to the length of R minus 1, x is the last element in R, q is 0, l is the first element in R, r is the last element in R, R has at least as many elements as the original value of t, and this is printed: either (a[r], r) if a[r] is greater than or equal to l, or [-1, -1] if a[r] is less than l, for each iteration of the loop.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n, a list of n integers, an integer q, and q pairs of integers. It then processes each test case by iterating through the list of integers and maintaining a list 'a' that keeps track of the last index where the current integer was first seen. After processing the list, it reads q pairs of integers and for each pair, it prints either the value at the corresponding index in list 'a' along with the index if the value is greater than or equal to the first integer in the pair, or [-1, -1] if the value is less than the first integer in the pair. The function continues this process until all test cases have been processed.

