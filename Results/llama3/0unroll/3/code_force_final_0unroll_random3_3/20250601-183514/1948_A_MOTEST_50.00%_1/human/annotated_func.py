#State of the program right berfore the function call: stdin contains two inputs: first an integer t (1 <= t <= 50) and then t lines each containing an integer n (1 <= n <= 50).
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
        
    #State: The output state is a series of strings, each representing a possible arrangement of uppercase ASCII letters. The number of strings is equal to the number of lines in the input, and each string is either 'NO' or a sequence of uppercase letters. If the input number is 1, the output is 'NO'. If the input number is even, the output is a sequence of uppercase letters where each letter appears twice. If the input number is odd, the output starts with 'AAA' and then follows the same pattern as the even case. The sequence of uppercase letters is determined by the ASCII order of the letters.

#Overall this is what the function does:This function reads a series of integers from standard input, generates and prints a corresponding series of strings, each representing a possible arrangement of uppercase ASCII letters. For each input integer, if it is 1, the function prints 'NO'. If the input integer is even, the function prints a sequence of uppercase letters where each letter appears twice, in ASCII order. If the input integer is odd, the function prints a sequence starting with 'AAA' followed by the same pattern as the even case. The function processes multiple input integers and prints the corresponding output strings.

