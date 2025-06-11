#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 50). The second line contains n integers k_1,k_2,...,k_n (2 ≤ k_i ≤ 20).
    t = int(input())
    for T in range(t):
        bets = int(input())
        
        a = [int(x) for x in input().split()]
        
        prod = 1
        
        for i in range(bets):
            prod *= a[i]
        
        sumo = 0
        
        for i in range(bets):
            a[i] = prod // a[i]
            sumo += int(a[i])
        
        if sumo >= prod:
            print(-1)
        else:
            ans = ''
            for i in range(bets):
                ans += str(a[i]) + ' '
            print(ans)
        
    #State: t is 0, T is t, bets is a non-negative integer, a is a list of integers with the value at index i changed to the product of its original value and all other integers in a divided by its original value, prod is the product of its original value and the values of a at indices 0 through bets-1, stdin contains no input, i is bets-1, sumo is the sum of the product of its original value and all other integers in a divided by its original value plus the integer value of a[i] for all i in range(bets). If sumo is greater than or equal to prod, -1 is printed. Otherwise, sumo is less than prod, ans is a string containing the string representation of the integer at index i of a followed by a space for all i in range(bets), and the string representation of all integers in the list a, each followed by a space is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n integers. It calculates the product of all integers in each test case, then for each integer, it calculates the product of all other integers divided by the current integer. If the sum of these calculated values is greater than or equal to the product of all integers, it prints -1. Otherwise, it prints the calculated values for each integer in the test case, separated by spaces.

