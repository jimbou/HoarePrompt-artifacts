#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 3 * 10^5) followed by n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
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
        
    #State: `n` is an integer between 1 and 3 * 10^5, `ar` is a list of `n` integers between 1 and `n`, `same` is 1, `num` is the last integer in `ar`, `i` is `len(ar)`, `minn` is the minimum of the previous minimum number of consecutive occurrences of any integer in `ar` and 1. If `minn` is infinity, -1 is printed. Otherwise, the minimum number of consecutive occurrences of any integer in `ar` which is `minn` is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n integers. It then finds the minimum number of consecutive occurrences of any integer in the list and prints this minimum value. If no such minimum value exists (i.e., all integers in the list appear only once), it prints -1. The function processes multiple test cases and prints the result for each case.

