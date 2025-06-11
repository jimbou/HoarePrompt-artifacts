#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t lines, each containing an integer n (1 <= n <= 50).
    os.system('cls')
    s = string.ascii_uppercase
    t = int(input())
    for i in range(t):
        n = int(input())
        
        if n == 1:
            print('NO')
        else:
            ans = ''
            x = 0
            if n % 2 == 0:
                for j in range(n // 2):
                    ans += s[x] * 2
                    x += 1
            else:
                ans, x = 'AAA', 1
                for j in range(n // 2 - 1):
                    ans += s[x] * 2
                    x += 1
            print('YES')
            print(ans)
        
    #State: Output State: The output state after the loop executes all the iterations is a series of lines, where each line is either 'NO' or 'YES' followed by a string of uppercase ASCII letters. The number of lines is equal to the initial value of t. For each line, if the corresponding input integer n is 1, the line is 'NO'. Otherwise, the line is 'YES' followed by a string of uppercase ASCII letters, where the length of the string is n, and the letters are arranged in a specific pattern based on whether n is even or odd. If n is even, the string consists of pairs of the same letter, starting from 'A' and incrementing the letter for each pair. If n is odd, the string starts with 'AAA' and then consists of pairs of the same letter, starting from 'B' and incrementing the letter for each pair.

#Overall this is what the function does:The function reads a series of integers from standard input, where the first integer t represents the number of subsequent integers. For each subsequent integer n, the function generates a string of uppercase ASCII letters based on whether n is even or odd. If n is 1, the function prints 'NO'. If n is even, the function prints 'YES' followed by a string of pairs of the same letter, starting from 'A' and incrementing the letter for each pair. If n is odd, the function prints 'YES' followed by a string starting with 'AAA' and then consisting of pairs of the same letter, starting from 'B' and incrementing the letter for each pair. The function repeats this process t times, printing the results for each integer.

