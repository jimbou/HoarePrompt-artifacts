#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains an integer n (1 <= n <= 50). The second line contains n integers k_1, k_2, ..., k_n (2 <= k_i <= 20).
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
        
    #State: Output State: The loop will execute `t` times, each time processing a test case. For each test case, it will read an integer `bets` and a list of `bets` integers from the input. It will then calculate the product of all the integers, and for each integer, it will calculate the product of all other integers by dividing the total product by the current integer. The sum of these products will be calculated. If the sum is greater than or equal to the total product, the loop will print `-1`. Otherwise, it will print the list of products separated by spaces. The loop will repeat this process for all `t` test cases.

#Overall this is what the function does:This function processes multiple test cases from standard input. For each test case, it reads an integer 'bets' and a list of 'bets' integers, calculates the product of all integers, and then for each integer, it calculates the product of all other integers. If the sum of these products is greater than or equal to the total product, it outputs -1. Otherwise, it outputs the list of products separated by spaces. This process is repeated for all test cases.

