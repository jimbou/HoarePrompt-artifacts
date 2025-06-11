#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains a single integer n (1 <= n <= 2*10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    t = int(input())
    for tc in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        maxsize = max(a)
        
        a.sort()
        
        mexsize = 1
        
        for sz in a:
            if sz == mexsize:
                mexsize = mexsize + 1
        
        if mexsize > maxsize:
            print('Alice' if mexsize % 2 == 0 else 'Bob')
        else:
            print('Alice' if mexsize % 2 == 1 else 'Bob')
        
    #State: t is an integer larger than 0, tc is t-1, stdin contains 0 test cases, n is an integer greater than 0, a is a sorted list of n integers, maxsize is the maximum integer in a, mexsize is the smallest positive integer that is not in a. Either 'Alice' or 'Bob' is printed depending on whether mexsize is even or odd.

#Overall this is what the function does:Determines the winner ('Alice' or 'Bob') for each of t test cases based on the smallest positive integer missing from a sorted list of n integers, printing the result for each case.

