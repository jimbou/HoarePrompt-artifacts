#State of the program right berfore the function call: **stdin contains multiple test cases. Each test case contains the following inputs:
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
        
    #State: t is 0, stdin contains no test cases, a is a list where the first element is 0 and the rest of the elements are 0 if the corresponding element in R() is equal to the previous element, otherwise the element is the index of the element in R() plus 1, p is the last value yielded by R(), i is the number of elements in R() plus 1, j is 0 if the last element in R() is equal to the second last element, otherwise j is the index of the last element in R() plus 1, q is 0, l is the first value yielded by R() in the last iteration, r is the second value yielded by R() in the last iteration, and the output of the program is either (a[r], r) or [-1, -1] for each iteration of the loop

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case contains a sequence of integers and a number of queries. For each test case, it processes the sequence of integers to create a list where each element is either 0 (if the corresponding integer is equal to the previous one) or the index of the integer plus 1 (if it's different). Then, it answers each query by printing either the value at the specified index in the list along with the index, or [-1, -1] if the value at the specified index is less than the query's first value. The function continues this process until all test cases have been read and processed, at which point it terminates with no remaining input in standard input.

