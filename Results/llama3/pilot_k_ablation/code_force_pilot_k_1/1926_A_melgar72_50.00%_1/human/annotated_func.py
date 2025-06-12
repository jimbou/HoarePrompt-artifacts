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
        
    #State: userString is a string of length 5 consisting of letters A and B, list(userString) is a list of characters in userString, countA is the number of 'A's in userString, countB is the number of 'B's in userString.
    if (countA > countB) :
        print('A')
        #This is printed: A
    else :
        if (countB > countA) :
            print('B')
            #This is printed: B
        else :
            pass
        #State: userString is a string of length 5 consisting of letters A and B, list(userString) is a list of characters in userString, countA is the number of 'A's in userString, countB is the number of 'B's in userString, countA is less than or equal to countB. If countB is greater than countA, 'B' is printed. Otherwise, countA is equal to countB.
    #State: *userString is a string of length 5 consisting of letters A and B, list(userString) is a list of characters in userString, countA is the number of 'A's in userString, countB is the number of 'B's in userString. If countA is greater than countB, 'A' is printed. If countA is less than countB, 'B' is printed. If countA is equal to countB, no character is printed.

#Overall this is what the function does:This function takes a string of length 5 consisting of letters A and B as input, counts the occurrences of 'A' and 'B', and prints the letter that appears more frequently. If both letters appear an equal number of times, it does not print anything.

