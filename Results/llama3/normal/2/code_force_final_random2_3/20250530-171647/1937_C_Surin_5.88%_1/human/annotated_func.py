#State of the program right berfore the function call: stdin contains one input: an integer (the number of test cases). Each test case consists of an integer (n) followed by n integers (p_0, p_1, ..., p_{n-1}) representing a permutation of integers from 0 to n-1.
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
        
    #State: The loop has executed for the number of test cases specified in the input, and the output is a series of strings in the format "! [prev] [v1]" where `prev` is the index of the maximum element in the array and `v1` is the index of the second maximum element in the array, and the output buffer has been flushed.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of an integer (n) followed by n integers representing a permutation of integers from 0 to n-1. For each test case, it finds the indices of the maximum and second maximum elements in the permutation and prints them in the format "! [prev] [v1]" to standard output, where `prev` is the index of the maximum element and `v1` is the index of the second maximum element. The function repeats this process for the specified number of test cases and ensures that the output buffer is flushed after each test case.

