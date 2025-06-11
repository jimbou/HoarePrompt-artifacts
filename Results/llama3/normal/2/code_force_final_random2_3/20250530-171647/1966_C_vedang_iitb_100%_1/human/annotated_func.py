#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 10^4). Each of the following t lines contains an integer n (1 <= n <= 2*10^5), and the next line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: mexsize is equal to maxsize + 1, n is an integer, a is a sorted list of integers, maxsize is the maximum value in a, stdin contains no inputs, tc is equal to t, and sz is the last element in a. If mexsize is greater than maxsize, 'Alice' is printed if mexsize is even, otherwise 'Bob' is printed. If mexsize is less than or equal to maxsize, 'Alice' is printed if mexsize is odd, otherwise 'Bob' is printed.

#Overall this is what the function does:This function determines the winner of a game based on the size of a list of integers. It reads multiple test cases from standard input, where each test case consists of a list of integers. For each test case, it sorts the list, finds the maximum size, and calculates the minimum excluded size (mexsize). If mexsize is greater than the maximum size, it prints 'Alice' if mexsize is even and 'Bob' if mexsize is odd. If mexsize is less than or equal to the maximum size, it prints 'Alice' if mexsize is odd and 'Bob' if mexsize is even. The function processes all test cases and prints the winner for each case.

