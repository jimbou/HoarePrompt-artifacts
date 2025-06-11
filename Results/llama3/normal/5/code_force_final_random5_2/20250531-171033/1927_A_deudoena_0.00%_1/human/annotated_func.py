#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case contains an integer n (1 <= n <= 10) followed by a string s of length n consisting of 'W' and 'B' characters, with at least one 'B' character.
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: inpstr is a string or list with at least len(inpstr) elements, i is len(inpstr)-1, j is the value of the last element of inpstr, ind1 is the index of the first 'B' in inpstr, ind2 is 0, outind is 0, stdin contains t-1 test cases, where t is the value of inpstr.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: inpstr is a string or list with at least len(inpstr) elements, i is 0, ind2 is the index of the first 'B' from the end of inpstr.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: len(inpstr) - ind2 - ind1 (where len(inpstr) is the length of inpstr, ind2 is the index of the first 'B' from the end of inpstr, and ind1 is the value of ind1)

#Overall this is what the function does:The function reads an integer t from standard input, followed by t test cases. Each test case consists of an integer n and a string s of length n containing 'W' and 'B' characters. The function then finds the indices of the first 'B' from the start and end of the string, and prints the length of the substring between these two indices (inclusive). The function repeats this process for all t test cases.

