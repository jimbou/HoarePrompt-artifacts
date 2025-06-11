#State of the program right berfore the function call: stdin contains one input: an integer (the number of test cases). Each test case consists of one integer (n) and a permutation p_0, p_1, \ldots, p_{n-1} of integers from 0 to n - 1.
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
        
    #State: kp is the number of test cases, n is an integer greater than or equal to 0, g is 0, v1 is an integer between 0 and n-1 inclusive, i is n-1, v2 is n-1, prev is n-1 if r is '>', otherwise prev is 0, I is a function that reads a list of integers from stdin, R is a function that reads a single integer from stdin, stdin contains at least 0 inputs, and the string "? 0 0 1 1", "? 1 1 2 2", ..., "? (n-2) (n-2) (n-1) (n-1)" are printed, and this is printed: "? [v1] [i] [v1] [prev]" where v1 is an integer between 0 and n-1 inclusive, i is n-1, and prev is n-1 if r is '>', otherwise prev is 0, and r is a string read from stdin, and this is printed: "! [prev] [v1]" where prev is n-1 if r is '>', otherwise prev is 0, and v1 is an integer between 0 and n-1 inclusive, and the output buffer is flushed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n and a permutation of integers from 0 to n-1. For each test case, it finds the maximum and second maximum elements in the permutation by querying the input in a specific format and prints the indices of these elements in the format "! prev v1". The function iterates over all test cases and performs the same operations for each case.

