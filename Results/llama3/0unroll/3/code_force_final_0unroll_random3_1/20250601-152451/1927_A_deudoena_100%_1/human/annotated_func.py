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
        
    #State: Output State: m is an integer, stdin contains multiple inputs: for each test case, first an integer (the length of the strip) and then a string consisting of 'W' and 'B' characters, ma is 0, mi is the position of the first 'B' in the string s, s is a string consisting of 'W' and 'B' characters, c is the length of the string s, d is 0, l is an empty list
    for j in s[::-1]:
        d += 1
        
        if j == 'B':
            ma = len(s) - d
            break
        
    #State: Output State: The loop has iterated over the string s in reverse order, and the variable d has been incremented by 1 in each iteration. The loop has stopped when it encountered the first 'B' character from the end of the string. The variable ma has been updated to the position of this 'B' character from the start of the string. The other variables remain unchanged.
    return ma - mi + 2
    #The program returns the difference between the position of the first 'B' character from the end of the string and the position of the first 'B' character from the start of the string, plus 2.

#Overall this is what the function does:Calculates the length of the shortest substring containing all 'B' characters in a given string, by finding the positions of the first 'B' characters from the start and end of the string, and returning their difference plus 2.

