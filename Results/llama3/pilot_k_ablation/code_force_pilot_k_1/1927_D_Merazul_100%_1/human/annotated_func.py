#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four inputs: first an integer, then a list of integers, then an integer, and then multiple pairs of integers. The first integer is the length of the list. The second integer is the number of pairs. Each pair contains two integers.
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
        
    #State: t is 0, a is a list of 0s and 1s, p is the second last element in R(), i is equal to the number of elements in R() minus 1, j is either 0 or 1 depending on whether the last element in R() is equal to the third last element in R(), q is 0, and the following has been printed for each iteration of the loop: either (a[r], r) if a[r] is not less than l, or [-1, -1] if a[r] is less than l, and this process has been repeated for the number of test cases equal to the initial value of t

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer, a list of integers, another integer, and multiple pairs of integers. It then processes each test case by creating a list 'a' of 0s and 1s based on the input list, and for each pair of integers, it prints either the value at the corresponding index in list 'a' along with the index, or [-1, -1] if the value at that index is less than the first integer in the pair. This process is repeated for the number of test cases specified at the beginning.

