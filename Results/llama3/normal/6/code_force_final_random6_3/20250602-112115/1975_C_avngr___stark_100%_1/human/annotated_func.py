#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains an integer n (2 <= n <= 10^5). The second line contains n space-separated integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The number of test cases is given on the first line of stdin (1 <= t <= 500).
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
        
    #State: t is 0, _ is t, n is an integer, a is a list of n integers, stdin contains no test cases, i is -1, temp is a sorted list of 3 integers from a starting at index n - 3, and max is the maximum of the second elements of all sorted sublists of 3 consecutive integers in a, and the maximum of the second elements of all sorted sublists of 3 consecutive integers in a which is max is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n space-separated integers. For each test case, it finds the maximum of the second elements of all sorted sublists of 3 consecutive integers in the list, and prints this maximum value. If a test case has only 2 integers, it prints the smaller of the two. After processing all test cases, the function concludes, leaving the input stream empty.

