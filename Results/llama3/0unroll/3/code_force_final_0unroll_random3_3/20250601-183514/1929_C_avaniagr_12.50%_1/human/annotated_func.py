#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three integers k, x, and a (k >= 2, 1 <= x <= 100, 1 <= a <= 10^9).
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
        
    #State: The output state will be a series of 'YES' or 'NO' printed to the console, each corresponding to the result of the conditional statements within the loop for each test case. The value of `t` will be unchanged, and the contents of `stdin` will be consumed.

#Overall this is what the function does:Determines whether a given number 'a' can be reached by a sequence of operations starting from 1, where each operation multiplies the current number by 'k' or adds 1, and prints 'YES' or 'NO' for each test case.

