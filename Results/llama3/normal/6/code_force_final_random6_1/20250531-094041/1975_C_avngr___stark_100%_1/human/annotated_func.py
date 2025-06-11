#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (2 <= n <= 10^5). The second line contains n space-separated integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The number of test cases t (1 <= t <= 500) is given before the test cases.
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        if n == 2:
            print(min(a))
            continue
        
        max = 0
        
        for i in range(n - 2):
            temp = a[i:i + 3]
            temp.sort()
            if temp[1] > max:
                max = temp[1]
        
        print(max)
        
    #State: t is an integer between 1 and 500 (inclusive), stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (2 <= n <= 10^5). The second line contains n space-separated integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9), and the maximum value of the second elements of all the sorted sublists of three consecutive integers from the list a which is max is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n space-separated integers. For each test case, it finds the maximum value of the second elements of all sorted sublists of three consecutive integers from the list, and prints this maximum value. If a test case has only two integers, it simply prints the smaller of the two. The function processes all test cases and prints the maximum values for each case.

