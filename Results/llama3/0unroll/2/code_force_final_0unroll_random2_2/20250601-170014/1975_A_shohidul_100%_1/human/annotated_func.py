#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (2 <= n <= 50) and then a list of n integers a_1,a_2,...,a_n (1 <= a_i <= 10^6).
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
        
    #State: The output state will be a series of 'YES' or 'NO' printed to the console, each corresponding to a test case. For each test case, if the list of integers is either already sorted in non-decreasing order or can be made sorted by removing a prefix of the list, 'YES' will be printed. Otherwise, 'NO' will be printed. The value of `t` will remain unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It checks if the list is already sorted in non-decreasing order or can be made sorted by removing a prefix of the list. For each test case, it prints 'YES' to the console if the list is sorted or can be made sorted, and 'NO' otherwise. The function processes all test cases and prints the corresponding results.

