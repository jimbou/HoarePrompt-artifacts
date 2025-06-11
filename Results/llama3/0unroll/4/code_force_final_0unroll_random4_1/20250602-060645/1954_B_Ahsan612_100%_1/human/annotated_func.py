#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains an integer n (1 <= n <= 3 * 10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
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
        
    #State: The output state will be a list of integers, where each integer represents the minimum number of consecutive equal elements in the corresponding test case. If no such minimum number exists (i.e., all elements in the test case are equal), the output will be -1.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a list of integers. It then finds the minimum number of consecutive equal elements in each list. If all elements in a list are equal, it outputs -1. Otherwise, it outputs the minimum number of consecutive equal elements. The function processes each test case independently and prints the results in the order they were received.

