#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer n (1 <= n <= 50). The second line contains n integers k_1,k_2,...,k_n (2 <= k_i <= 20).
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
        
    #State: t is equal to 0, T is equal to t, bets is a non-negative integer, a is a list of integers where the value at index i is the integer division of the product of the initial value of prod (1) and all the values of a[i] for i in range bets by the original value of a[i], i is equal to bets, sumo is the sum of the integer division of the product of the initial value of prod (1) and all the values of a[i] for i in range bets by the original value of a[i] for all i in range bets, prod is the product of the initial value of prod (1) and all the values of a[i] for i in range bets, stdin contains no input. If the current value of sumo is greater than or equal to the current value of prod, -1 is printed. Otherwise, bets is a positive integer, and the string ans containing all elements of a followed by a space is being printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a number of bets and a list of integers. It calculates the product of the integers and then replaces each integer with the product divided by the original integer. If the sum of these new integers is greater than or equal to the product, it prints -1. Otherwise, it prints the new list of integers. The function continues this process until all test cases have been read from standard input.

