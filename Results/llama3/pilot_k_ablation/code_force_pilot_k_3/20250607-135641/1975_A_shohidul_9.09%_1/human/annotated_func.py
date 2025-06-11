#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (2 <= n <= 50). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^6).
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
        
    #State: t is 0, n is an integer equal to the input value, a is a list of n integers from the input, check_all is a boolean indicating whether all elements in a are in increasing order, _ is t, stdin is empty. If check_all is True, 'YES' is printed. Otherwise, check_all is updated to True if all elements in new are less than a[0], False otherwise. If a[i - 1] > a[i], then if check_all and new_all are both True, 'YES' is printed and we break out of the most internal loop or if statement. Otherwise, we break out of the most internal loop or if statement. If a[i - 1] <= a[i], nothing changes.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n integers. It checks if the integers are in increasing order. If they are, it prints 'YES'. If not, it checks if the remaining integers (after the first decreasing pair) are in increasing order and all less than the first integer. If this condition is met, it prints 'YES'; otherwise, it prints 'NO'. The function processes all test cases and then terminates, leaving the input stream empty.

