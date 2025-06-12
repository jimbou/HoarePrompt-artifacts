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
        #State: *userString is a string of length 5 consisting of letters A and B, list(userString) is a list of characters in userString, countA is the number of 'A's in userString, countB is the number of 'B's in userString, and countA is less than or equal to countB. If countB is greater than countA, 'B' is printed. If countB is less than or equal to countA, no printing occurs.
    #State: *userString is a string of length 5 consisting of letters A and B, list(userString) is a list of characters in userString, countA is the number of 'A's in userString, countB is the number of 'B's in userString. If countA is greater than countB, 'A' is printed. If countA is less than or equal to countB, then if countB is greater than countA, 'B' is printed. Otherwise, no printing occurs.

#Overall this is what the function does:Counts the occurrences of 'A' and 'B' in a given string of length 5, and prints 'A' if 'A' occurs more frequently, 'B' if 'B' occurs more frequently, and nothing if they occur equally.

