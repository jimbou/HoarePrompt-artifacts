#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers k, x, and a (2 <= k <= 30, 1 <= x <= 100, 1 <= a <= 10^9).
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
        
    #State: The output state will be a series of 'YES' or 'NO' printed to the console, one for each test case, indicating whether the given conditions are met or not. The value of 't' remains unchanged, and the values of 'k', 'x', and 'a' are updated for each test case. The final state will have the same 't' value, but the values of 'k', 'x', and 'a' will be the last set of values read from the input for the last test case.

#Overall this is what the function does:Determines whether a given set of conditions are met for multiple test cases and prints 'YES' or 'NO' to the console for each case. The function accepts no parameters and returns no values, instead, it reads input from the standard input and prints output to the console. The conditions are based on the values of three integers k, x, and a, and the function performs different checks depending on the value of x relative to k. The final state of the program is the same as the initial state, with the only change being the output printed to the console.

