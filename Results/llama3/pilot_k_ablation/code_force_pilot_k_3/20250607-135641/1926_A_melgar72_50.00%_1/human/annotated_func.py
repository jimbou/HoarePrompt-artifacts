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
        
    #State: `userString` is a string of length 5 consisting of letters A and B, `countA` is equal to the number of 'A's in `userString`, `countB` is equal to the number of 'B's in `userString`, a list representation of `userString` exists in memory, and the current value of `letter` is the last character in `userString`.
    if (countA > countB) :
        print('A')
        #This is printed: A
    else :
        if (countB > countA) :
            print('B')
            #This is printed: B
        else :
            pass
        #State: *`userString` is a string of length 5 consisting of letters A and B, `countA` is equal to the number of 'A's in `userString`, `countB` is equal to the number of 'B's in `userString`, a list representation of `userString` exists in memory, and the current value of `letter` is the last character in `userString`. Additionally, if `countB` is greater than `countA`, 'B' is being printed. Otherwise, `countA` is greater than or equal to `countB`.
    #State: *`userString` is a string of length 5 consisting of letters A and B, `countA` is equal to the number of 'A's in `userString`, `countB` is equal to the number of 'B's in `userString`, a list representation of `userString` exists in memory, and the current value of `letter` is the last character in `userString`. If `countA` is greater than `countB`, 'A' is printed. If `countB` is greater than `countA`, 'B' is printed. If `countA` is equal to `countB`, no printing occurs.

#Overall this is what the function does:Counts the occurrences of 'A' and 'B' in a given string of length 5, consisting only of letters A and B, and prints 'A' if 'A' occurs more frequently, 'B' if 'B' occurs more frequently, and does nothing if they occur equally.

