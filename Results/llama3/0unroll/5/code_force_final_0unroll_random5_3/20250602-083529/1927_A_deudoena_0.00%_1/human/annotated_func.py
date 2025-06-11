#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 10) and then a string s of length n consisting of 'W' and 'B' characters. There is at least one 'B' in s.
    inpstr = input()
    ind1 = 0
    ind2 = 0
    outind = 0
    for (i, j) in enumerate(inpstr):
        if j == 'B':
            ind1 = i
            break
        
    #State: Output State: The loop iterates over the string inpstr and finds the index of the first occurrence of the character 'B'. If 'B' is found, the loop breaks and the index of 'B' is stored in ind1. If 'B' is not found, the loop completes all iterations and ind1 remains unchanged. The values of ind2 and outind remain unchanged as they are not affected by the loop.
    for i in range(len(inpstr)):
        if inpstr[-i - 1] == 'B':
            ind2 = i
            break
        
    #State: Output State: The loop iterates over the string inpstr and finds the index of the first occurrence of the character 'B' from the end of the string. If 'B' is found, the loop breaks and the index of 'B' is stored in ind2. If 'B' is not found, the loop completes all iterations and ind2 remains unchanged. The values of ind1 and outind remain unchanged as they are not affected by the loop.
    print(len(inpstr) - ind2 - ind1)
    #This is printed: len(inpstr) - ind2 - ind1 (where ind2 is the index of the first occurrence of 'B' from the end of inpstr and ind1 is the value of ind1)

#Overall this is what the function does:This function reads a string of 'W' and 'B' characters from standard input, finds the indices of the first and last occurrences of 'B', and prints the length of the substring between these two indices (inclusive).

