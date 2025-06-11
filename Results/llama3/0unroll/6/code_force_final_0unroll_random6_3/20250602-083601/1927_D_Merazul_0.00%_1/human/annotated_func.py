#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains four inputs: first an integer, then a list of integers, then an integer, and then a list of pairs of integers. The first integer is the length of the list of integers. The second integer is the number of pairs of integers. The list of integers contains integers between 1 and 10^6. The list of pairs of integers contains pairs of integers between 1 and the length of the list of integers. The sum of the lengths of the lists of integers across all test cases does not exceed 2 * 10^5. The sum of the numbers of pairs of integers across all test cases does not exceed 2 * 10^5.
    R = lambda : map(int, input().split())
    t, = R()
    while t:
        t -= 1
        
        *_, k = R()
        
        a = {*R()}
        
        b = {*R()}
        
        f = 1
        
        m = n = k // 2
        
        for i in range(1, k + 1):
            u = i in a
            v = i in b
            f &= u | v
            m -= u & ~v
            n -= ~u & v
        
        print('YNEOS'[f ^ 1 or m | n < 0::2])
        
    #State: Output State: t is 0, stdin is empty, and the output contains a string of 'Y's and 'N's for each test case.
    #
    #In this output state, the loop has executed all the iterations, and the variable t has been decremented to 0. The stdin has been consumed, and it is now empty. The output contains a string of 'Y's and 'N's, where each character corresponds to the result of a test case. 'Y' indicates that the given conditions are satisfied, and 'N' indicates that they are not.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer, a list of integers, another integer, and a list of pairs of integers. It then checks for each test case whether the given conditions are satisfied, specifically whether the intersection of the list of integers and the list of pairs of integers meets certain criteria. The function outputs a string of 'Y's and 'N's, where 'Y' indicates that the conditions are satisfied for a test case and 'N' indicates that they are not. The function consumes all input from standard input and produces a corresponding output string.

