#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains a single integer n (1 <= n <= 3 * 10^5), and the line after that contains n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
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
        
    #State: `n` is an integer, `ar` is a list of integers, `same` is the number of consecutive occurrences of the last element of `ar`, `num` is the last element of `ar`, `i` is equal to the length of `ar`, `minn` is the minimum number of consecutive occurrences of any element in `ar`, `_` is equal to the number of iterations of the loop, stdin is empty. If `minn` is either infinity or equal to the length of `ar`, then -1 is printed. Otherwise, the minimum number of consecutive occurrences of any element in `ar` which is `minn` is printed.

#Overall this is what the function does:This function reads multiple lines of input from stdin, where the first line contains the number of test cases, and each test case consists of a line with an integer n followed by a line with n integers. It then finds the minimum number of consecutive occurrences of any element in each test case and prints this minimum number, or -1 if all elements are the same or if there is only one element.

