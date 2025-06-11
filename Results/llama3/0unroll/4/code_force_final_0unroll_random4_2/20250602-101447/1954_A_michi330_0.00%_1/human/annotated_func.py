#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 1000) and then t lines each containing three integers n, m and k (1 <= m, k <= n <= 50).
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) < k:
            print('NO')
        else:
            print('Yes')
        
    #State: The output state will contain 't' number of lines, each containing either 'YES' or 'NO'. 'YES' will be printed if the given conditions are met, otherwise 'NO' will be printed. The value of 't' remains unchanged.

#Overall this is what the function does:Determines whether a given set of conditions is met for a series of test cases and prints 'YES' or 'NO' accordingly. The function takes no parameters and returns no value, instead printing the results directly to the output. It processes a variable number of test cases, each defined by three integers (n, m, k), and evaluates whether the conditions n > k and n - ceil(n/m) >= k are both true. If both conditions are met, it prints 'YES'; otherwise, it prints 'NO'. The function does not modify the input values and does not retain any state between test cases.

