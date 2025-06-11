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
        
    #State: Output State: The loop has executed all its iterations, and the output state is the final state after the last iteration of the loop. The values of the variables in the loop head and body have been updated accordingly. The state of the other variables in the precondition that are not affected by the loop head and body remains unchanged.

#Overall this is what the function does:The function reads an integer from standard input, representing the number of test cases. For each test case, it reads another integer 'n' and performs a series of queries to find the maximum and second maximum values in a range from 1 to 'n'. It then prints the indices of these maximum and second maximum values. The function repeats this process for each test case, updating the output state after each iteration.

