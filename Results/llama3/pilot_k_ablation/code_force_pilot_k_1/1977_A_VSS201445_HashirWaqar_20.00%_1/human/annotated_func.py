#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two integers n and m (1 <= n, m <= 100).
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        if n < m:
            print('NO')
        elif n & 1 and m & 1 or n % 2 == 0 and m % 2 == 0:
            print('YES')
        
    #State: The loop has executed for a number of times equal to the integer t. For each iteration, if n is less than m, 'NO' is printed. If n is not less than m, and both n and m are either both odd or both even, 'YES' is printed. Otherwise, no action is taken. The values of n and m are not stored after the loop finishes. The loop will not execute if the input does not contain an integer t followed by t lines, each containing two integers n and m.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of two integers, n and m. For each test case, it checks if n is less than m and prints 'NO' if true. If n is not less than m, it checks if both n and m are either both odd or both even, and prints 'YES' if the condition is met. If neither condition is met, it takes no action. The function does not store the values of n and m after processing each test case. The function will only execute if the input is in the correct format, consisting of an integer t followed by t lines, each containing two integers n and m.

