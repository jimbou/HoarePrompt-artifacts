#State of the program right berfore the function call: stdin contains one input: an integer (the number of test cases). Each test case consists of an integer (n) followed by a permutation p_0, p_1, ..., p_{n-1} of integers from 0 to n - 1.
    I = lambda : list(map(int, input().split(' ')))
    R = lambda : int(input())
    for kp in range(int(input())):
        n = int(input())
        
        g = 0
        
        v1 = 0
        
        for i in range(1, n):
            v2 = i
            print(f'? {v1} {v1} {v2} {v2}')
            sys.stdout.flush()
            r = input('')
            if r == '<':
                v1 = v2
        
        prev = 0
        
        for i in range(1, n):
            print(f'? {v1} {i} {v1} {prev}')
            sys.stdout.flush()
            r = input()
            if r == '>':
                prev = i
        
        print(f'! {prev} {v1}')
        
        sys.stdout.flush()
        
    #State: stdin contains no input, I is a function that takes no arguments and returns a list of integers, R is a function that takes no arguments and returns an integer, kp is undefined, n is undefined, g is undefined, v1 is undefined, v2 is undefined, prev is undefined, r is undefined, i is undefined.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a permutation of integers from 0 to n-1. For each test case, it finds the maximum element in the permutation and its index, and then prints the index and the maximum element to standard output. The function repeats this process for all test cases, and finally, it flushes the standard output buffer to ensure all output is displayed.

