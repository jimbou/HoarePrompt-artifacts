#State of the program right berfore the function call: stdin contains multiple inputs: first an integer t (1 <= t <= 10^4), then for each test case, first an integer n (1 <= n <= 10), then a string s of length n consisting of 'W' and 'B' characters, with at least one 'B' character.
    ma = mi = 0
    m = int(input())
    s = input()
    c = d = 0
    l = []
    for j in s:
        c += 1
        
        if j == 'B':
            mi = c
            break
        
    #State: m is an integer between 1 and 10^4, ma is 0, mi is the position of the first 'B' character in the string s, s is a string of length n consisting of 'W' and 'B' characters, c is n, d is 0, l is an empty list, stdin contains multiple inputs: for each test case, first an integer n (1 <= n <= 10), then a string s of length n consisting of 'W' and 'B' characters, with at least one 'B' character.
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: m is an integer between 1 and 10^4, ma is either 0 or n - d, mi is the position of the first 'B' character in the string s, s is a string of length n consisting of 'W' and 'B' characters with at least one character, c is n, d is n, l is an empty list, stdin contains multiple inputs: for each test case, first an integer n (1 <= n <= 10), then a string s of length n consisting of 'W' and 'B' characters, with at least one 'B' character, j is the first character in the string s. If j is 'B', then ma is 0, otherwise ma is n - d.
    return ma - mi + 2
    #The program returns a value that is the difference between ma and mi plus 2, where ma is either 0 or n - d, mi is the position of the first 'B' character in the string s, and n is the length of the string s.

#Overall this is what the function does:The function takes no arguments and returns the length of the shortest substring of 'B' characters in a given string of 'W' and 'B' characters, plus 2. It reads input from stdin, where the first input is an integer t (1 <= t <= 10^4) representing the number of test cases, followed by t test cases. Each test case consists of an integer n (1 <= n <= 10) representing the length of the string, and a string s of length n consisting of 'W' and 'B' characters, with at least one 'B' character. The function returns the length of the shortest substring of 'B' characters in the string s, plus 2, for each test case.

