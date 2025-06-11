#State of the program right berfore the function call: stdin contains multiple inputs: first an integer (the number of test cases), then for each test case, first an integer (the length of the strip) and then a string consisting of 'W' and 'B' characters.
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
        
    #State: Output State: m is an integer, s is a string consisting of 'W' and 'B' characters, ma is 0, mi is the position of the first 'B' character in s, c is the position of the first 'B' character in s, d is 0, l is an empty list, stdin contains multiple inputs: for each test case, first an integer (the length of the strip) and then a string consisting of 'W' and 'B' characters.
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: Output State: m is an integer, s is a string consisting of 'W' and 'B' characters, ma is the position of the last 'B' character in s, mi is the position of the first 'B' character in s, c is the position of the first 'B' character in s, d is the position of the last 'B' character in s plus one, l is an empty list, stdin contains multiple inputs: for each test case, first an integer (the length of the strip) and then a string consisting of 'W' and 'B' characters.
    return ma - mi + 2
    #The program returns the difference between the position of the last 'B' character and the position of the first 'B' character in string s, plus 2.

#Overall this is what the function does:Calculates and returns the length of the substring containing 'B' characters in a given string, including the first and last 'B' characters, by finding the positions of the first and last 'B' characters and returning their difference plus 2.

