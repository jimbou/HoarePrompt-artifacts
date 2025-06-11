#State of the program right berfore the function call: stdin contains multiple test cases. Each test case consists of two lines. The first line contains an integer n (1 <= n <= 10). The second line contains a string s of length n, consisting of characters 'W' and 'B', with at least one 'B'.
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: inpstr is the first line of the first test case, i is the length of inpstr minus 1, ind1 is the index of the last 'B' in inpstr, ind2 is 0, outind is 0, and stdin contains the remaining test cases.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: inpstr is a string with at least 1 character, i is the length of inpstr minus 1, ind1 is the index of the last 'B' in inpstr, ind2 is the index of the first 'B' from the end of inpstr, outind is 0, and stdin contains the remaining test cases.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: the number of characters between the first and last occurrences of the character 'B' in the string inpstr

#Overall this is what the function does:This function reads a string from standard input, finds the first and last occurrences of the character 'B' in the string, and prints the number of characters between these two occurrences. The function assumes that the input string contains at least one 'B' and does not modify the input string.

