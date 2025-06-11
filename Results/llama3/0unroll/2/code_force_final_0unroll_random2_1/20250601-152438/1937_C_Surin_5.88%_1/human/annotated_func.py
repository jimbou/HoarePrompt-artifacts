#State of the program right berfore the function call: stdin contains one input: an integer (the number of test cases). Each test case consists of an integer (n) followed by a sequence of n integers (p_0, p_1, ..., p_{n-1}) that is a permutation of integers from 0 to n-1.
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
        
    #State: Output State: The loop has executed for the specified number of test cases, and for each test case, it has determined the maximum value in the range [1, n] and the index of the maximum value in the range [1, n]. The loop has printed the results for each test case in the format '! index max_value'. The state of the other variables, such as stdin, I, and R, remains unchanged.

#Overall this is what the function does:Determines the index and maximum value of a sequence of integers for multiple test cases and prints the results.

