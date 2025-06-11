#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (2 <= n <= 50). The second line contains n integers (1 <= a_i <= 10^6).
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
        
    #State: t is an integer between 2 and 50 (inclusive), stdin is empty, n is an integer between 2 and 50 (inclusive), a is a list of n integers (1 <= a_i <= 10^6), check_all is a boolean value indicating whether all elements in a are in increasing order, _ is t.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. It checks if the list is in increasing order, and if not, it checks if the list can be split into two parts such that the first part is in decreasing order and the second part is in increasing order. The function prints 'YES' if the list meets either condition, and 'NO' otherwise.

