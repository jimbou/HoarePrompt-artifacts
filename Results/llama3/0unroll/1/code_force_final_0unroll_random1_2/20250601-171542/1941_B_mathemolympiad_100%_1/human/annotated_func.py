#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (3 <= n <= 2 * 10^5) followed by a space-separated list of n integers a_1, a_2, ..., a_n (0 <= a_j <= 10^9).
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
        
    #State: The output state after the loop executes all the iterations will be a series of 'YES' or 'NO' printed to the console, indicating whether each test case can be solved by subtracting operations from the array elements. The number of 'YES' or 'NO' printed will be equal to the number of test cases (numTest). The values of numTest and the input test cases will remain unchanged.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It then attempts to solve each test case by subtracting operations from the array elements, and prints 'YES' if the test case can be solved and 'NO' otherwise. The function processes all test cases and prints the corresponding 'YES' or 'NO' for each case, without modifying the input values.

