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
        
    #State: The output state will be a series of lines, each containing either -1 or a sequence of integers separated by spaces. The number of lines will be equal to the value of t. For each test case, if the sum of the modified integers (each integer divided by the product of all integers) is greater than or equal to the product of all integers, the output will be -1. Otherwise, the output will be a sequence of modified integers, each representing the result of dividing the product of all integers by the respective integer.

#Overall this is what the function does:This function processes multiple test cases from standard input, each containing a set of integers. For each test case, it calculates the product of all integers and then modifies each integer by dividing the product by the integer itself. If the sum of these modified integers is greater than or equal to the product, it outputs -1. Otherwise, it outputs the sequence of modified integers. The function repeats this process for all test cases provided in the input, producing a series of output lines corresponding to each test case.

