#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains an integer n (1 <= n <= 2*10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
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
        
    #State: t is an integer greater than or equal to 0, i is equal to t, n is an integer, lis is a sorted list of unique integers. If 1 is not in lis or the length of lis is 1, then 'Alice' is printed. If 1 is in lis and the length of lis is more than 1, then either 'Bob' or 'Alice' is printed depending on whether the difference between any two consecutive elements of lis is greater than 1 and the index of the second element is odd or even, or whether the length of lis is odd or even and test is True. If test is False, no additional action is taken.

#Overall this is what the function does:This function reads input from stdin, processes t test cases, and determines the winner ('Alice' or 'Bob') based on the given conditions. For each test case, it reads an integer n and a list of n integers, removes duplicates, and sorts the list. If the list contains only one element or does not contain 1, it prints 'Alice'. Otherwise, it checks for gaps in the list and prints 'Bob' if a gap is found at an odd index or 'Alice' if a gap is found at an even index. If no gaps are found, it prints 'Alice' if the length of the list is odd and 'Bob' if the length is even.

