#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains a single integer n (1 <= n <= 2*10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The number of test cases is given on the first line of stdin.
    t = int(input())
    for i in range(t):
        n = int(input())
        
        l = map(int, input().split())
        
        lis = sorted(set(l))
        
        if 1 not in lis or len(lis) == 1:
            print('Alice')
        else:
            test = True
            for j in range(1, len(lis)):
                if lis[j] - lis[j - 1] > 1:
                    if j % 2 == 1:
                        print('Bob')
                    else:
                        print('Alice')
                    test = False
                    break
            if test == True:
                if len(lis) % 2 == 1:
                    print('Alice')
                else:
                    print('Bob')
        
    #State: t is an integer between 0 and 2*10^5, i is equal to t, n is an integer equal to the input value, lis is a sorted list of unique integers from the input, stdin contains no test cases, test is unchanged. If 1 is not in lis or the length of lis is 1, 'Alice' is printed. If 1 is in lis and the length of lis is greater than 1, then if the difference between two consecutive elements in lis is not greater than 1, 'Alice' is printed if the length of lis is odd, and 'Bob' is printed if the length of lis is even. Otherwise, the state of the variables remains unchanged.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n integers. It processes each test case by removing duplicates, sorting the numbers, and then determining the winner of a game based on the sequence of numbers. If the sequence starts with 1 and all consecutive numbers are either the same or differ by 1, the winner is determined by the length of the sequence (Alice wins if the length is odd, Bob wins if it's even). Otherwise, the winner is determined by the first pair of consecutive numbers that differ by more than 1 (Bob wins if the first number of the pair is odd, Alice wins if it's even). The function prints the winner's name for each test case.

