#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains a single integer n (1 ≤ n ≤ 50). The second line contains n integers k_1,k_2,…,k_n (2 ≤ k_i ≤ 20).
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
        
    #State: The output state after the loop executes all the iterations is that the variable 't' remains unchanged, stdin is empty, and the console contains the output of the loop for each test case. For each test case, if the sum of the modified array elements is greater than or equal to the product of the original array elements, the console contains '-1'. Otherwise, the console contains the modified array elements separated by spaces.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of a single integer n followed by n integers. It calculates the product of these integers, then for each integer, it calculates the product of all other integers and sums these values. If the sum is greater than or equal to the product of all integers, it prints -1; otherwise, it prints the modified array elements separated by spaces. The function processes all test cases and prints the corresponding output for each case.

