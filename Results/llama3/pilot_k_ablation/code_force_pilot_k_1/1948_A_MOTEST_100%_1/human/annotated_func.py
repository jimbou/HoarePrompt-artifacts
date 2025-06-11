#State of the program right berfore the function call: stdin contains two inputs: first an integer (between 1 and 50 inclusive) and then a series of integers (between 1 and 50 inclusive).
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
        
    #State: `s` is the string of all uppercase English letters, `t` is an integer between 1 and 50 inclusive, `i` is equal to `t`, stdin contains no input. For each even integer `n` input, 'YES' is printed, and the string consisting of the first n/2 uppercase English letters each repeated twice is printed. For each odd integer `n` input, 'NO' is printed.

#Overall this is what the function does:This function reads a series of integers from standard input, where the first integer specifies the number of subsequent integers to process. For each subsequent integer, if it is even, the function prints 'YES' followed by a string consisting of the first half of the uppercase English alphabet, with each letter repeated twice. If the integer is odd, the function prints 'NO'. The function processes all input integers and then terminates, leaving the standard input empty.

