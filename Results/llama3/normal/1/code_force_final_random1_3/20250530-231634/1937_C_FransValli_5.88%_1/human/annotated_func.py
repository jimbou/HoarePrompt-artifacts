#State of the program right berfore the function call: stdin contains one input: an integer (the number of test cases). Each test case contains one input: an integer (the size of the permutation).
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
        
    #State: `n` is at least 2, `i` is `n`, `k` is `n-1`, `res` is a string containing the input, `best` is the maximum value of `i` for which `res` is '<', and stdin is empty, and this is printed: '!', k which is n-1, best which is the maximum value of `i` for which `res` is '<'

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case represents the size of a permutation. For each test case, it iteratively queries the permutation to find the second-largest element and then prints the indices of the largest and second-largest elements in the format '!, k, best'. The function repeats this process for all test cases until standard input is empty.

