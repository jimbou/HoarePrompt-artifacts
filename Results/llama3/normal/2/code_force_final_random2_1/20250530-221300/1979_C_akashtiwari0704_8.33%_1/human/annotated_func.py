#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains a single integer n (1 ≤ n ≤ 50). The second line contains n integers k_1, k_2, …, k_n (2 ≤ k_i ≤ 20).
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
        
    #State: t is 0, T is t, bets is an integer, a is a list of integers where the ith element is the integer division of prod by the new value of a[i], prod is the product of all elements in a except the ith element, i is bets - 1, sumo is the original value of sumo plus the sum of the integer divisions of prod by the original value of a[i] for all i in range(bets), stdin is empty. If sumo is greater than or equal to prod, then -1 is printed. Otherwise, a string containing the ith element of a followed by a space, repeated bets times, is printed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a number of bets and a list of integers. It calculates the product of all integers in each test case, then for each integer, it calculates the product of all other integers and adds this to a sum. If the sum is greater than or equal to the product, it prints -1; otherwise, it prints a string containing the calculated products for each integer, separated by spaces.

