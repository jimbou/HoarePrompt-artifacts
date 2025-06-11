#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 3 * 10^5) followed by a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
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
        
        if minn == inf or minn == len(ar):
            print(-1)
        else:
            print(minn)
        
    #State: The output state contains t lines, each containing an integer. The integer on each line is the minimum number of consecutive equal elements in the corresponding list of integers. If no such number exists (i.e., all elements in the list are equal), the output is -1.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a list of integers. It then analyzes each list to find the minimum number of consecutive equal elements. If all elements in the list are equal, it outputs -1. Otherwise, it outputs the minimum count of consecutive equal elements. The function processes multiple test cases and prints the result for each case on a separate line.

