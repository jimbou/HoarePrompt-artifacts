#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 3 * 10^5) followed by a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= n) such that the list is beautiful. The sum of n over all test cases does not exceed 3 * 10^5.
    for _ in range(int(input())):
        n = int(input())
        
        ar = list(map(int, input().split()))
        
        same = 1
        
        num = ar[0]
        
        minn = inf
        
        i = 1
        
        while i < len(ar):
            if ar[i] == num:
                same += 1
            else:
                i += 1
                num = ar[i]
                minn = min(minn, same)
                same = 1
            i += 1
        
        minn = min(minn, same)
        
        if minn == inf:
            print(-1)
        else:
            print(minn)
        
    #State: `same` is the number of times the most frequent integer appears in `ar`, `num` is the most frequent integer in `ar`, `minn` is the minimum of the minimum number of times any integer appears in `ar` and the number of times the most frequent integer appears in `ar`, `i` is `n`, `stdin` contains `0` test cases, and `_` is `t`. If `minn` is infinity, -1 is printed. Otherwise, the minimum of the minimum number of times any integer appears in `ar` and the number of times the most frequent integer appears in `ar` which is `minn` is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It then finds the minimum frequency of any integer in the list and prints this value. If the list is empty or no integer appears more than once, it prints -1. The function processes all test cases and prints the minimum frequency for each case.

