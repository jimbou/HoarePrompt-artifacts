#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines of input. The first line contains an integer n (2 <= n <= 50). The second line contains n space-separated integers a_i (1 <= a_i <= 10^6).
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
        
    #State: The loop will execute t times, and for each execution, it will read two lines of input from stdin. The first line will contain an integer n, and the second line will contain n space-separated integers a_i. The loop will then check if the list a_i is sorted in non-decreasing order. If it is, the loop will print 'YES'. If it's not, the loop will check if the list can be sorted by removing some elements from the beginning. If it can, the loop will print 'YES'. If it can't, the loop will print 'NO'. After all iterations, the loop will finish, and the program will terminate.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n space-separated integers. It checks if the integers are sorted in non-decreasing order. If they are, it prints 'YES'. If not, it checks if the list can be sorted by removing some elements from the beginning. If it can, it prints 'YES'. If it cannot, it prints 'NO'. The function repeats this process for each test case and then terminates.

