#State of the program right berfore the function call: stdin contains an integer t (1 ≤ t ≤ 10^4) followed by t test cases. Each test case contains an integer n (1 ≤ n ≤ 10) followed by a string s of length n consisting of characters 'W' and 'B', with at least one 'B'.
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
        
    #State: m is an integer between 1 and 10^4, ma is 0, mi is the position of the first 'B' in the string s, s is a string of length between 1 and 10 consisting of characters 'W' and 'B' with at least one 'B', c is the length of the string s, d is 0, l is an empty list, stdin contains m-1 integers and m-1 strings of length between 1 and 10 consisting of characters 'W' and 'B' with at least one 'B', j is the last character in the string s.
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: `m` is an integer between 1 and 10^4, `ma` is the position of the last 'B' in the string `s`, `mi` is the position of the first 'B' in the string `s`, `s` is a string of length between 1 and 10 consisting of characters 'W' and 'B' with at least one 'B', `c` is the length of the string `s`, `d` is the length of the string `s`, `l` is an empty list, `stdin` contains `m-1` integers and `m-1` strings of length between 1 and 10 consisting of characters 'W' and 'B' with at least one 'B', and the current value of `j` is the first character in the string `s`.
    return ma - mi + 2
    #The program returns the difference between the position of the last 'B' and the position of the first 'B' in the string `s`, plus 2, where `s` is a string of length between 1 and 10 consisting of characters 'W' and 'B' with at least one 'B'.

#Overall this is what the function does:This function calculates and returns the length of the shortest substring containing all 'B's in a given string of 'W's and 'B's, where the string length is between 1 and 10 and contains at least one 'B'. The function takes no parameters and returns an integer value representing the length of the shortest substring plus 2.

