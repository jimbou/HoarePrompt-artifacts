#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 10) followed by a string s of length n consisting of 'W' and 'B' characters, with at least one 'B' character.
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: ind1 is the index of the first 'B' character in inpstr, ind2 is 0, outind is 0, stdin contains t-1 test cases. Each test case contains an integer n (1 <= n <= 10) followed by a string s of length n consisting of 'W' and 'B' characters, with at least one 'B' character.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: ind1 is the index of the first 'B' character in inpstr, ind2 is the index of the last 'B' character in inpstr, outind is 0, stdin contains t-1 test cases.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: length of inpstr minus the sum of indices of the first and last 'B' characters in inpstr

#Overall this is what the function does:The function reads an integer t from standard input, followed by t test cases. Each test case consists of an integer n and a string s of length n containing 'W' and 'B' characters. The function finds the indices of the first and last 'B' characters in the string s and prints the length of the string minus the sum of these indices. The function repeats this process for all t test cases.

