#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then for each test case, first an integer n (3 <= n <= 2 * 10^5), then a space-separated list of n integers a_1, a_2, ..., a_n (0 <= a_j <= 10^9).
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
        
    #State: numTest is an integer between 0 and 10^4 (inclusive), n is an integer that must be at least 3, a is a list of integers where a[i] is 0 for all i in range(0, n - 2), a[i + 1] is reduced by 3 times the original value of a[i] and then by 2 times the original value of a[i] for all i in range(0, n - 3), a[i + 2] is reduced by the original value of a[i] and then by the original value of a[i] for all i in range(0, n - 3), i is n - 2. If the last two elements of a are both 0, 'YES' is printed. Otherwise, if the last two elements of a are not both 0, 'NO' is printed. If stop is True, we skip to the next iteration of the loop. Otherwise, no changes are made.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It then attempts to reduce the list of integers to zeros by iteratively subtracting the current element from the next two elements. If the last two elements of the list can be reduced to zeros, it prints 'YES'; otherwise, it prints 'NO'. If any element in the list is negative, it immediately prints 'NO' and skips to the next test case. The function repeats this process for all test cases.

