#State of the program right berfore the function call: stdin contains two inputs: first an integer (the number of test cases) and then a list of integers (the number of special characters for each test case). Each integer is greater than or equal to 1 and less than or equal to 50.
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
        
    #State: Output State: s is the string of all uppercase ASCII letters, t is an integer equal to 0, stdin is empty.

#Overall this is what the function does:This function reads input from stdin, processes it, and prints output to the console. It takes no parameters and returns no value. The function clears the console, reads an integer (t) representing the number of test cases, and then reads a list of integers (n) representing the number of special characters for each test case. For each test case, if n is 1, it prints 'NO'. Otherwise, it constructs a string (ans) by repeating uppercase ASCII letters in a specific pattern and prints 'YES' followed by the constructed string. After processing all test cases, the function leaves the console in a cleared state with no remaining input in stdin.

