#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (3 <= n <= 2 * 10^5) followed by n integers a_1, a_2, ..., a_n (0 <= a_j <= 10^9).
    numTest = int(input())
    for _ in range(0, numTest):
        n = int(input())
        
        a = [int(x) for x in input().split()]
        
        stop = False
        
        for i in range(0, n - 2):
            if a[i] < 0:
                print('NO')
                stop = True
                break
            opNum = a[i]
            a[i] -= opNum
            a[i + 1] -= 2 * opNum
            a[i + 2] -= opNum
        
        if stop == True:
            continue
        
        if a[len(a) - 1] != 0 or a[len(a) - 2] != 0:
            print('NO')
        else:
            print('YES')
        
    #State: The output state will contain 'YES' or 'NO' for each test case, indicating whether the given array can be reduced to all zeros by the specified operations. The value of `numTest` will be the same as the initial state, and the stdin will be empty as all test cases would have been processed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an array of integers. It attempts to reduce each array to all zeros by applying a specific operation, which subtracts a value from the current element, twice that value from the next element, and the same value from the element after that. If the array can be reduced to all zeros, it prints 'YES'; otherwise, it prints 'NO'. The function processes all test cases and prints the result for each case.

