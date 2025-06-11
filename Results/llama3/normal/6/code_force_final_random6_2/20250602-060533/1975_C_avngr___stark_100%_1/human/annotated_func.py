#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer n (2 <= n <= 10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The number of test cases t (1 <= t <= 500) is given in the first line of stdin.
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
        
    #State: t is an integer between 0 and 500 inclusive, _ is t, n is an integer and is at least 2, a is a list of n integers between 1 and 10^9 inclusive, stdin contains 0 test cases, i is n-2, temp is a list of 3 integers between 1 and 10^9 inclusive, sorted in ascending order, and max is the maximum value of temp[1] after all iterations of the loop, and the maximum value of temp[1] which is max is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n and a list of n integers. It then finds the maximum value of the middle element of all possible sublists of three consecutive integers in the list, excluding the case where n is 2, in which case it simply prints the smaller of the two integers. The function prints the maximum middle value for each test case.

