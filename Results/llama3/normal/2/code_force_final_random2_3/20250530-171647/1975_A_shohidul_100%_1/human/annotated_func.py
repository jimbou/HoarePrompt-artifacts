#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains an integer n (2 <= n <= 50). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6).
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        check_all = all([(a[i - 1] <= a[i]) for i in range(1, n)])
        
        if check_all:
            print('YES')
        else:
            for i in range(1, n):
                if a[i - 1] > a[i]:
                    new = a[i:]
                    check_all_new = all([(a[0] >= new[i]) for i in range(len(new))])
                    new_all = all([(new[i - 1] <= new[i]) for i in range(1, len(new))])
                    if check_all_new and new_all:
                        print('YES')
                        break
                    else:
                        print('NO')
                        break
        
    #State: t is an integer between 0 and 49 (inclusive), n is an integer between 2 and 50 (inclusive), a is a list of n integers (1 <= a_i <= 10^6), check_all is a boolean indicating whether the list a is sorted in non-decreasing order. If check_all is true, 'YES' is printed. Otherwise, if a is sorted in non-decreasing order and the first element of a is greater than or equal to all elements in a new list new, and new is sorted in non-decreasing order, then the program breaks out of the most internal loop or if statement. Otherwise, 'NO' is printed, and the program breaks out of the most internal loop or if statement.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It checks if the list is sorted in non-decreasing order. If the list is sorted, it prints 'YES'. If the list is not sorted, it checks if the first element is greater than or equal to all elements in the unsorted part of the list and if the unsorted part is sorted in non-decreasing order. If both conditions are met, it prints 'YES'. Otherwise, it prints 'NO'. The function processes all test cases and prints the corresponding results.

