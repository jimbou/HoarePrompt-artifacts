#State of the program right berfore the function call: stdin contains one input: an integer (t) (1 <= t <= 10^3), followed by t test cases. Each test case contains one integer (n) (2 <= n <= 10^4).
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
        
    #State: The output state is a series of print statements, each containing either a question mark (?) or an exclamation mark (!) followed by four space-separated integers. The number of print statements is equal to the number of test cases (t) multiplied by the number of iterations of the inner loops (which is n-1 for the first inner loop and n-1 for the second inner loop). The integers in each print statement are the values of the variables v1, v1, v2, v2, or prev, v1, i, prev, depending on the iteration of the inner loops. The final print statement for each test case contains an exclamation mark (!) followed by the values of prev and v1.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case contains an integer (n) representing the number of elements. For each test case, it performs a series of comparisons and prints the results in the form of question marks (?) or exclamation marks (!) followed by four space-separated integers. The function ultimately prints the values of two variables, prev and v1, for each test case, which represent the result of the comparisons. The function does not return any value but instead prints the results directly to the standard output.

