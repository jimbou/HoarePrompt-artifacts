#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: the first input is an integer (n >= 2), the second and third inputs are strings of length n consisting of '<' and '>' characters.
    for j in range(int(input())):
        n = int(input())
        
        a = input()
        
        b = input()
        
        for i in range(1, n, 2):
            if i + 1 < n and a[i] == b[i + 1] == '<' or a[i] == b[i - 1] == '<':
                print('NO')
                break
        else:
            print('YES')
        
    #State: `j` is the number of test cases, `n` is not defined, `a` is not defined, `b` is not defined, stdin is empty, `i` is not defined.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (n) and two strings (a and b) of length n, containing '<' and '>' characters. It then checks if the strings satisfy a specific condition: for every odd-indexed character in the strings, if the character at that index and the character at the next index in the other string are both '<', or if the character at that index and the character at the previous index in the other string are both '<', it prints 'NO' and moves on to the next test case. If no such condition is found, it prints 'YES'. The function processes all test cases and leaves the standard input empty.

