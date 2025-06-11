#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (n) and then a list of n integers. n is an integer such that 2 <= n <= 50. The integers in the list are between 1 and 10^6.
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
        
    #State: t is an integer greater than or equal to 0, n is an integer, a is a list of n integers, and check_all is a boolean value. If check_all is True, 'YES' is printed. If check_all is False, then for each i in the range [1, n), if a[i - 1] is greater than a[i], either 'YES' or 'NO' has been printed and the loop has been exited. Otherwise, the loop has completed all iterations without printing anything, and i is set to n - 1.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It checks if the list is non-decreasing, and if not, it checks if the list can be made non-decreasing by removing a prefix of elements. The function prints 'YES' if the list is non-decreasing or can be made non-decreasing, and 'NO' otherwise.

