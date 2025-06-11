#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t test cases. Each test case contains an integer n (2 <= n <= 10^4) followed by n integers p_0, p_1, ..., p_{n-1} representing a permutation of integers from 0 to n-1.
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
        
    #State: The output state is a series of lines, each containing either a question mark (?) or an exclamation mark (!) followed by four space-separated integers. The question mark lines represent queries to the input, and the exclamation mark lines represent the final answer for each test case. The final answer for each test case is a pair of integers, where the first integer is the index of the maximum element in the permutation, and the second integer is the index of the second maximum element in the permutation. The output state does not contain the input integers t, n, and p_0, p_1, ..., p_{n-1}.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case represents a permutation of integers. For each test case, it queries the input to find the maximum and second maximum elements in the permutation and outputs the indices of these elements. The function performs a series of comparisons to determine the maximum and second maximum elements, and it outputs the results in a specific format, with each result consisting of a pair of indices.

