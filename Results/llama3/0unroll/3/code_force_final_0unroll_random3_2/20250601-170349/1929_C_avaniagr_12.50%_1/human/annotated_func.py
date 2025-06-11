#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing three integers k, x, and a (2 <= k <= 30, 1 <= x <= 100, 1 <= a <= 10^9).
    t = int(input())
    for _ in range(t):
        k, x, a = map(int, input().split())
        
        if x < k - 1:
            if a >= x + 1:
                print('YES')
            else:
                print('NO')
        elif x == k - 1:
            if a >= x + 3:
                print('YES')
            else:
                print('NO')
        else:
            z = 0
            for i in range(x + 1):
                z += z // (k - 1) + 1
            if a >= z:
                print('YES')
            else:
                print('NO')
        
    #State: The output state will contain t lines, each containing either 'YES' or 'NO', indicating whether the given conditions are met for each set of input values k, x, and a.

#Overall this is what the function does:This function determines whether a given set of conditions are met for each of multiple input sets, where each set consists of three integers k, x, and a. It reads the number of input sets t from standard input, followed by t lines, each containing k, x, and a. For each set, it checks if a is greater than or equal to a calculated value based on k and x, and prints 'YES' if the condition is met, or 'NO' otherwise. The calculated value depends on the values of k and x, with different formulas applied for different ranges of x relative to k. The function outputs t lines, each containing either 'YES' or 'NO', indicating whether the condition is met for each input set.

