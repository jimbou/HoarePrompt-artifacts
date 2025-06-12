#State of the program right berfore the function call: stdin contains t test cases. Each test case contains two lines. The first line contains a single integer n (1 <= n <= 2*10^5). The second line contains n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        s = set()
        
        for i in range(n):
            s.add(arr[i])
        
        s = list(s)
        
        ans = 1
        
        s = [0] + s
        
        n = len(s)
        
        if n == 2:
            print('Alice')
        else:
            for i in range(1, n - 1):
                if s[i] - s[i - 1] > 1:
                    break
                else:
                    ans = 1 - ans
            if ans:
                print('Alice')
            else:
                print('Bob')
        
    #State: stdin is empty, n is the number of unique elements in the last test case plus 1, arr is a list of integers of the last test case, s is a list of unique elements of the last test case with a 0 prepended, i is n-1, ans is either 0 or 1 depending on whether the number of pairs of adjacent elements in s with a difference of 1 is even or odd, and either 'Alice' or 'Bob' has been printed for each test case.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of a list of integers. It determines the winner of a game based on the number of pairs of adjacent unique elements with a difference of 1. If the number of such pairs is even, 'Alice' wins; otherwise, 'Bob' wins. The function prints the winner for each test case and empties the standard input.

