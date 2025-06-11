#State of the program right berfore the function call: stdin contains multiple lines of input: the first line contains a positive integer, then multiple pairs of lines follow, where the first line of each pair contains a positive integer and the second line contains a string consisting of 'W' and 'B' characters.
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
        
    #State: Output State: ma is 0, mi is the position of the first 'B' in s, m is a positive integer, s is a string consisting of 'W' and 'B' characters, c is the position of the first 'B' in s, d is 0, l is an empty list, stdin contains multiple pairs of lines: the first line of each pair contains a positive integer and the second line contains a string consisting of 'W' and 'B' characters.
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: Output State: ma is the position of the last 'B' in s, mi is the position of the first 'B' in s, m is a positive integer, s is a string consisting of 'W' and 'B' characters, c is the position of the first 'B' in s, d is the position of the last 'B' in s, l is an empty list, stdin contains multiple pairs of lines: the first line of each pair contains a positive integer and the second line contains a string consisting of 'W' and 'B' characters.
    return ma - mi + 2
    #The program returns the difference between the position of the last 'B' and the position of the first 'B' in string s, plus 2.

#Overall this is what the function does:This function reads input from stdin, processes the first pair of lines, and returns the difference between the position of the last 'B' and the position of the first 'B' in the second line of the pair, plus 2. The function does not modify the input or produce any side effects. It only consumes the first two lines of stdin and returns a calculated value based on the positions of 'B' characters in the second line.

