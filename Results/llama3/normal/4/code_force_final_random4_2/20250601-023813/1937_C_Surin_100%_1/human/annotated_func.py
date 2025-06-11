#State of the program right berfore the function call: stdin contains one input: an integer (the number of test cases). Each test case consists of one integer (n) followed by n integers (a permutation of integers from 0 to n - 1).
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
            elif r == '=':
                print(f'? {i} {i} {prev} {prev}')
                sys.stdout.flush()
                r2 = input('')
                if r2 == '<':
                    prev = i
        
        print(f'! {prev} {v1}')
        
        sys.stdout.flush()
        
    #State: The loop finishes executing when `kp` reaches the value returned by `int(input())`, at which point `n` is an integer, `g` is 0, `v1` is `n-1`, `i` is `n-1`, `v2` is `n-1`, `kp` is equal to the value returned by `int(input())`, `prev` is either `n-1` or `n-2` depending on the values of `r` and `r2`, and the output buffer contains various printed messages based on the values of `r` and `r2`, and this is printed: "! [prev] [n-1]" where `prev` is the value of `prev` which is either `n-1` or `n-2` depending on the values of `r` and `r2`, and `n-1` is the value of `v1`. The output buffer is flushed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer n followed by a permutation of integers from 0 to n-1. For each test case, the function determines the maximum and second-maximum values in the permutation and prints them to standard output in the format "! max second_max". The function uses a series of queries to the input stream to compare elements of the permutation and determine the maximum and second-maximum values. The function repeats this process for each test case until the input is exhausted.

