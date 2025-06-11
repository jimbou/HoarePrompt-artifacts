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
            elif r == '=':
                print(f'? {i} {i} {prev} {prev}')
                sys.stdout.flush()
                r2 = input('')
                if r2 == '<':
                    prev = i
        
        print(f'! {prev} {v1}')
        
        sys.stdout.flush()
        
    #State: The output buffer has been flushed, the variables `I`, `R`, `g`, and `kp` remain in their initial state, `n` is an integer, `v2` is `n-1`, `i` is `n-1`, `r` and `r2` are strings containing the input values, and `prev` and `v1` are integers between 0 and `n-1`. The following has been printed for each iteration: "? [v1] [i] [v1] [prev]" and "! [prev] [v1]".

#Overall this is what the function does:The function reads an integer from standard input, then iterates through a range of numbers from 1 to the input integer. For each iteration, it prints a series of queries in the format "? [v1] [i] [v1] [prev]" and reads the input values. Based on the input values, it updates the values of `prev` and `v1`. Finally, it prints a result in the format "! [prev] [v1]" and flushes the output buffer. The function repeats this process for a number of iterations specified by the initial input integer.

