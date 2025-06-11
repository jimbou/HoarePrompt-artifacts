#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (2 <= n <= 50) and then a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        check_all = all([(a[i - 1] < a[i]) for i in range(1, n)])
        
        if check_all:
            print('YES')
        else:
            for i in range(1, n):
                if a[i - 1] > a[i]:
                    new = a[i:]
                    check_all = all([(a[0] > new[i]) for i in range(len(new))])
                    new_all = all([(new[i - 1] <= new[i]) for i in range(1, len(new))])
                    if check_all and new_all:
                        print('YES')
                        break
                    else:
                        print('NO')
                        break
        
    #State: The output state after the loop executes all the iterations is a series of 'YES' or 'NO' printed to the console, indicating whether the input list of integers is sorted in ascending order or not. The number of 'YES' or 'NO' printed is equal to the value of 't', which is the number of test cases. The value of 't' remains unchanged, as it is not affected by the loop head and body. The input list of integers 'a' is also unchanged, as it is not modified by the loop. The variables 'n', 'check_all', 'new', 'check_all', and 'new_all' are local to the loop and do not affect the output state.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It checks if the list is sorted in ascending order. If the list is sorted, it prints 'YES'. If the list is not sorted, it checks if the list can be sorted by removing a prefix of elements. If such a prefix exists, it prints 'YES'. Otherwise, it prints 'NO'. The function processes all test cases and prints the corresponding 'YES' or 'NO' for each case.

