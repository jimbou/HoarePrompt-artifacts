#State of the program right berfore the function call: userString is a string of length 5 consisting of letters A and B.
    list(userString)
    countA = 0
    countB = 0
    for letter in userString:
        if letter == 'A':
            countA += 1
        elif letter == 'B':
            countB += 1
        else:
            continue
        
    #State: Output State: userString is a string of length 5 consisting of letters A and B, countA is 3, countB is 2, and a list representation of userString exists in memory.
    if (countA > countB) :
        print('A')
        #This is printed: A
    else :
        if (countB > countA) :
            print('B')
            #This is printed: B
        else :
            pass
        #State: *userString is a string of length 5 consisting of letters A and B, countA is 3, countB is 2, and a list representation of userString exists in memory. If countB is greater than countA, 'B' is printed. Otherwise, countA is greater than or equal to countB.
    #State: userString is a string of length 5 consisting of letters A and B, countA is 3, countB is 2, and a list representation of userString exists in memory. If countA is higher than countB, the letter 'A' is printed. If countB is higher than countA, the letter 'B' is printed. Otherwise, countA is greater than or equal to countB.

#Overall this is what the function does:This function takes a string of length 5 consisting of letters A and B as input, counts the occurrences of each letter, and prints the letter that appears more frequently. If both letters appear with the same frequency, it does not print anything. The function does not modify the input string.

