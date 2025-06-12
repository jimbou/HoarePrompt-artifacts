#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (2 <= n <= 50) and then a list of n integers (1 <= a_i <= 10^6).
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
        
    #State: t is 0, stdin is empty, _ is t-1, n is an integer (2 <= n <= 50), a is a list of n integers, check_all is either True or False, 'YES' or 'NO' has been printed for each test case.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It checks if the list is sorted in ascending order. If the list is sorted, it prints 'YES'. If the list is not sorted, it checks if the unsorted part of the list (from the first pair of elements that are in the wrong order to the end) can be sorted in ascending order and if the first element of the original list is greater than all elements in the unsorted part. If both conditions are met, it prints 'YES'. Otherwise, it prints 'NO'. The function processes all test cases and prints a 'YES' or 'NO' result for each one.

