#State of the program right berfore the function call: stdin contains one integer t (1 <= t <= 1000) followed by t lines, each containing three integers n, m, and k (1 <= m, k <= n <= 50).
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) < k:
            print('NO')
        else:
            print('Yes')
        
    #State: The output will be a series of 'YES' or 'NO' printed to the console, with the number of lines equal to the value of t. Each line will correspond to the result of the condition check for the respective input values of n, m, and k. The values of t, n, m, and k will remain unchanged, as they are only used within the loop and do not affect the overall state.

#Overall this is what the function does:This function reads a series of input values from the standard input, where the first line contains an integer t, representing the number of test cases, followed by t lines, each containing three integers n, m, and k. It then evaluates a condition for each set of input values and prints 'YES' if the condition is met, and 'NO' otherwise. The condition checks if n is greater than k and if n minus the ceiling of n divided by m is greater than or equal to k. The function prints the result of each condition check to the console, with the number of lines equal to the value of t.

