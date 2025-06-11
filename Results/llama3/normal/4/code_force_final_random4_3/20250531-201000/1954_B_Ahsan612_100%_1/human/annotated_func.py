#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 3 * 10^5) followed by a list of n integers a_1, a_2, ..., a_n (1 <= a_i <= n).
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
        
    #State: `n` is an integer, `ar` is a list of integers, `same` is either 1 or the length of the longest sequence of equal elements in `ar`, `num` is the last element of `ar`, `i` is equal to the length of `ar`, `stdin` contains 0 test cases, and `_` is equal to `t`. If the minimum of the length of the shortest sequence of equal elements in `ar` and `same` is either infinity or equal to the length of `ar`, then -1 is printed. Otherwise, the minimum of the length of the shortest sequence of equal elements in `ar` and `same` is printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by a list of n integers. It then finds the length of the shortest sequence of equal elements in the list and prints this length, unless the list contains only one unique element or the shortest sequence is the entire list, in which case it prints -1.

