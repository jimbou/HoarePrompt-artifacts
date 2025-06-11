#State of the program right berfore the function call: stdin contains one input: an integer (the number of test cases), followed by a sequence of test cases. Each test case consists of one integer (the size of the permutation), followed by a sequence of n integers (the permutation).
    for _ in range(int(input())):
        n = int(input())
        
        k = 1
        
        for i in range(2, n):
            print('?', 0, k, 0, i, flush=True)
            res = input()
            if res == '<':
                k = i
        
        best = 0
        
        for i in range(1, n):
            print('?', k, best, k, i, flush=True)
            res = input()
            if res == '<':
                best = i
        
        print('!', k, best, flush=True)
        
    #State: The output state after the loop executes all the iterations is a sequence of test cases, where each test case consists of a single integer (the size of the permutation), followed by a sequence of n integers (the permutation), where the permutation is sorted in ascending order.

#Overall this is what the function does:This function reads a sequence of test cases from standard input, where each test case consists of a permutation of integers. It then sorts each permutation in ascending order and prints the sorted permutation to standard output. The function iterates over each test case, comparing pairs of elements to determine the correct order, and outputs the sorted result in the format specified by the problem.

