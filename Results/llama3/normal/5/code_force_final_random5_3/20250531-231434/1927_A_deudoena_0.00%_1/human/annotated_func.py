#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t test cases. Each test case consists of an integer n (1 <= n <= 10) followed by a string s of length n consisting of 'W' and 'B' characters, with at least one 'B' character.
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: inpstr is a string that must have at least n characters, j is the last character in the string, i is n-1, stdin contains t-1 test cases. If j is 'B', then ind1 is n-1 and ind2 is 0. Otherwise, the values of ind1 and ind2 are not changed.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: inpstr is a string that must have at least n characters, i is n-1, j is the last character in the string, stdin contains t-1 test cases. If the last character of inpstr is 'B', then ind2 is n-1 and ind1 is 0. Otherwise, the values of ind1 and ind2 are not changed.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: the length of inpstr minus the sum of ind2 and ind1 (where the length of inpstr is at least n characters, ind2 is n-1 if the last character of inpstr is 'B' otherwise its value is not changed, and ind1 is 0 if the last character of inpstr is 'B' otherwise its value is not changed)

#Overall this is what the function does:This function reads an integer t from standard input, followed by t test cases. Each test case consists of an integer n and a string s of length n containing 'W' and 'B' characters. It then finds the first and last occurrences of 'B' in the string and prints the length of the string minus the sum of the indices of these two 'B's. If 'B' is not found at the start or end of the string, it uses the index of the first or last 'B' found, respectively. The function does not modify the input string or any external state, and its output is solely based on the input provided.

