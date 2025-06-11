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
        
    #State: numTest is an integer (0 <= numTest <= 10^4) and the current value of numTest is 0, n is an integer (3 <= n <= 2 * 10^5), a is a list of n integers with modified elements, i is n - 2, stdin contains 0 test cases, a[i] is 0, a[i + 1] is decreased by three times the original value of a[i], a[i + 2] is decreased by the original value of a[i]. If stop is True, we skip to the next iteration of the loop. Otherwise, no changes are made. If the last element of a is not 0 or the second last element of a is not 0, 'NO' is printed. If the last two elements of the list a are both 0, 'YES' is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a list of integers. It then attempts to modify the list by subtracting a certain value from each element and its neighbors, in a way that makes the last two elements of the list equal to zero. If successful, it prints 'YES'; otherwise, it prints 'NO'. The function repeats this process for each test case, and once all test cases have been processed, it terminates.

