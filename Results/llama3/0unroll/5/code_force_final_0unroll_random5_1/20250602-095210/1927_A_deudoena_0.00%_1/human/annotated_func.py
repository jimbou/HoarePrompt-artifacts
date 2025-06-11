#State of the program right berfore the function call: stdin contains t+2t lines, where t is a positive integer. The first line contains a positive integer t. The next 2t lines are organized in t groups of two lines. The first line of each group contains a positive integer n. The second line of each group contains a string of length n, consisting of 'W' and 'B' characters, with at least one 'B' character.
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: Output State: The loop iterates over the string inpstr, which is a positive integer t. For each character j in inpstr, it checks if j is equal to 'B'. If it is, it sets ind1 to the index i of that character and breaks out of the loop. Therefore, after the loop executes all the iterations, ind1 will be set to the index of the first 'B' character in inpstr, and ind2 and outind will remain unchanged at 0.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: Output State: The loop iterates over the string inpstr, which is a positive integer t. For each character j in inpstr, it checks if j is equal to 'B'. If it is, it sets ind2 to the index i of that character and breaks out of the loop. Therefore, after the loop executes all the iterations, ind2 will be set to the index of the first 'B' character in inpstr, and ind1 and outind will remain unchanged at 0.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: the length of the string inpstr minus the index of the first 'B' character in inpstr minus 0

#Overall this is what the function does:The function reads a string of 'W' and 'B' characters from standard input, finds the indices of the first and last 'B' characters, and prints the length of the substring between these two indices (inclusive).

