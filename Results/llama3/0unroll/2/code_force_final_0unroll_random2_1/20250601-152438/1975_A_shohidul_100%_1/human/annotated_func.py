#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains an integer n (2 <= n <= 50). The second line contains n integers (1 <= a_i <= 10^6).
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
        
    #State: The output state is a series of 'YES' or 'NO' strings, each corresponding to a test case. If the input list is already sorted in ascending order, the output is 'YES'. If not, the code checks if there is a point where the list can be split into two sorted parts, with the first part being in descending order and the second part being in ascending order. If such a point exists, the output is 'YES'; otherwise, it is 'NO'. The number of 'YES' or 'NO' strings is equal to the value of 't', which is the number of test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n integers. It checks if the integers are sorted in ascending order. If they are, it prints 'YES'. If not, it checks if there is a point where the list can be split into two sorted parts, with the first part being in descending order and the second part being in ascending order. If such a point exists, it prints 'YES'; otherwise, it prints 'NO'. The function processes all test cases and prints the corresponding 'YES' or 'NO' strings for each case.

