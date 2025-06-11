#State of the program right berfore the function call: stdin contains one input: an integer (greater than 0).
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
        
    #State: The loop has finished executing, and the output state is determined by the final values of the variables in the loop head and body.

#Overall this is what the function does:The function reads a series of integers from standard input, where each integer represents the number of elements in a sequence. For each sequence, it performs a series of comparisons and outputs the indices of the maximum element in the sequence. The function iterates over multiple sequences, as specified by the initial input, and outputs the results for each sequence.

