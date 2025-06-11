#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four inputs: first an integer, then a list of integers, then an integer, and then multiple pairs of integers. The first integer is the length of the list. The second integer is the number of pairs. The pairs are such that the first integer of each pair is less than the second integer of the pair and both are less than or equal to the length of the list.
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
        
    #State: t is 0, stdin is empty, a is a list of integers, p is the last integer in the list, i is the length of the list, j is the index of the last integer in the list that is not equal to p, q is 0, l and r are the last pair of integers read from stdin.

#Overall this is what the function does:This function reads multiple test cases from standard input, processes each test case by creating a list of integers and then answers queries about the list. For each query, it prints the value of the element at the specified index in the list if it is greater than or equal to a given value, otherwise it prints -1. The function continues this process until all test cases have been processed, at which point it has read all input from standard input and has printed the results of all queries.

