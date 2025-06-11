#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 2*10^5) and then n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9). The number of test cases is between 1 and 10^4.
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
        
    #State: Output State: The output state after the loop executes all the iterations is a series of strings, either 'Alice' or 'Bob', each corresponding to the result of the game for each test case. The number of strings is equal to the initial value of `t`. The value of `t` remains unchanged.

#Overall this is what the function does:This function determines the winner of a game for each test case in the input, where the game involves finding the smallest positive integer (mexsize) not present in a sorted list of integers (a). If mexsize is greater than the maximum value in the list (maxsize), the winner is determined by whether mexsize is even or odd. Otherwise, the winner is determined by whether mexsize is odd or even. The function prints the winner ('Alice' or 'Bob') for each test case.

