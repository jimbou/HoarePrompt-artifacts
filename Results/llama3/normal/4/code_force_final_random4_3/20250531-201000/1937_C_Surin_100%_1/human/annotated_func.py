#State of the program right berfore the function call: stdin contains one input: an integer (t) (1 <= t <= 10^3), then t times an integer (n) (2 <= n <= 10^4).
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
        
    #State: n is an integer (1 <= n <= 10^3), i is n, g is 0, kp is t-1, v2 is n-1, prev is either 0 or n-1 or i, v1 is n-1, r is a string containing one character ('>', '=', or '<'), r2 is either '<' or an empty string, and the output "! [prev] [v1]" where prev is either 0 or n-1 or i and v1 is n-1 is flushed to the standard output.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer (t) represents the number of test cases, and each test case consists of an integer (n) representing the size of a sequence. For each test case, the function performs a series of queries to determine the maximum and second maximum elements in the sequence, and then outputs the indices of these two elements in the format "! [prev] [v1]", where prev is the index of the maximum element and v1 is the index of the second maximum element. The function repeats this process for each test case.

