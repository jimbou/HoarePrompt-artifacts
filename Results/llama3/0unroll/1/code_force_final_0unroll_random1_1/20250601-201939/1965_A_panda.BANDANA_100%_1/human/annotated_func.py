#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains an integer n. The second line contains n space-separated integers. t is a positive integer, n is a positive integer, and the integers on the second line are positive integers.
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
        
    #State: The output state will be a series of 'Alice' or 'Bob' printed to the console, one for each test case. The output will depend on the input values and the logic of the loop. Specifically, for each test case, if the set of unique integers does not contain 1 or has only one element, 'Alice' will be printed. Otherwise, the loop will check the differences between consecutive unique integers. If a difference greater than 1 is found, 'Bob' will be printed if the index of the larger integer is odd, and 'Alice' will be printed if the index is even. If no such difference is found, 'Alice' will be printed if the number of unique integers is odd, and 'Bob' will be printed if it is even.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer n followed by n space-separated integers. It then determines the winner of a game based on the unique integers in each test case, printing 'Alice' or 'Bob' to the console for each test case. The winner is determined by the presence of 1 in the unique integers, the number of unique integers, and the differences between consecutive unique integers. If 1 is not present or there is only one unique integer, 'Alice' wins. Otherwise, the function checks the differences between consecutive unique integers, and if a difference greater than 1 is found, the winner is determined by the index of the larger integer. If no such difference is found, the winner is determined by the parity of the number of unique integers.

