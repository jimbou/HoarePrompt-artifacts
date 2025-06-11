#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (2 <= n <= 50) and then a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6).
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
        
    #State: _ is t, n is an integer, a is a list of integers, check_all is a boolean value indicating whether the list a is sorted in ascending order. If check_all is true, 'YES' is printed. If check_all is false, then if a[i - 1] > a[i] for any i in range(1, n), and both check_all_new and new_all are true, 'YES' has been printed, and the most internal loop or if statement is exited. If a[i - 1] is not greater than a[i] for all i in range(1, n), then no action is taken.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It checks if the list is sorted in ascending order. If the list is sorted, it prints 'YES'. If the list is not sorted, it checks if the unsorted part of the list (from the first pair of elements that are in the wrong order to the end) is sorted and if the first element of the unsorted part is not greater than the first element of the original list. If both conditions are met, it prints 'YES'. Otherwise, it prints 'NO'.

