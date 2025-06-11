#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t integers n (1 <= n <= 50).
    os.system('cls')
    s = string.ascii_uppercase
    t = int(input())
    for i in range(t):
        n = int(input())
        
        if n % 2 == 1:
            print('NO')
        else:
            ans, x = '', 0
            x = 0
            for j in range(n // 2):
                ans += s[x] * 2
                x += 1
            print('YES')
            print(ans)
        
    #State: The loop will have executed t times, printing 'YES' or 'NO' for each iteration, and if 'YES', it will also print a string of uppercase ASCII letters, with each letter repeated twice, and the letters are chosen from the string s in a cyclic manner, starting from the first letter 'A'. The stdin will be empty after the loop finishes.

#Overall this is what the function does:The function reads a series of inputs from stdin, where the first input is an integer t, representing the number of test cases, followed by t integers n. For each n, it checks if n is even or odd. If n is odd, it prints 'NO'. If n is even, it prints 'YES' and generates a string of uppercase ASCII letters, with each letter repeated twice, chosen from the string 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' in a cyclic manner, starting from 'A'. The function prints the result for each test case and empties the stdin after processing all test cases.

