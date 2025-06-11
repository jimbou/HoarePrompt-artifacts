#State of the program right berfore the function call: stdin contains a series of test cases. Each test case contains a line with a single integer n, a line with n space-separated integers, a line with a single integer q, and q lines with two space-separated integers each. All integers are in the range [1, 2*10^5] and the sum of n and q across all test cases does not exceed 2*10^5.
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
        
    #State: t is 0, stdin contains an empty series of test cases, a is a set of unique integers, b is a set of unique integers, f is 1 if all i from 1 to k are in a or b, otherwise 0, m is k // 2 minus the number of i from 1 to k that are in a and not in b, otherwise k // 2, n is k // 2 minus the number of i from 1 to k that are in b and not in a, otherwise k // 2, k is an integer greater than or equal to 0, i is k, u is True if k is in a, otherwise False, v is True if k is in b, otherwise False, and 'YNEOS'[f ^ 1 or m | n < 0::2] is printed for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a set of integers and a set of queries. It then checks if all integers from 1 to k are present in either of the sets, and if the difference between the number of integers in the first set and the number of integers in the second set is within a certain range. If both conditions are met, it prints 'YES', otherwise it prints 'NO'. The function continues this process until all test cases have been processed, at which point the standard input is empty.

