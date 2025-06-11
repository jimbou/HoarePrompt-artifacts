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
        
    #State: `userString` is a string of length 5 consisting of letters A and B, `countA` is the number of 'A's in `userString`, `countB` is the number of 'B's in `userString`, `list(userString)` is a list of characters in `userString`.
    if (countA > countB) :
        print('A')
        #This is printed: A
    else :
        if (countB > countA) :
            print('B')
            #This is printed: B
        else :
            pass
        #State: *`userString` is a string of length 5 consisting of letters A and B, `countA` is the number of 'A's in `userString`, `countB` is the number of 'B's in `userString`, `list(userString)` is a list of characters in `userString`. If `countB` is greater than `countA`, then 'B' is printed. If `countA` is equal to `countB`, then no action is taken.
    #State: *`userString` is a string of length 5 consisting of letters A and B, `countA` is the number of 'A's in `userString`, `countB` is the number of 'B's in `userString`, `list(userString)` is a list of characters in `userString`. If `countA` is greater than `countB`, then 'A' is printed. If `countB` is greater than `countA`, then 'B' is printed. If `countA` is equal to `countB`, then no action is taken.

#Overall this is what the function does:This function takes a string of length 5 consisting of letters A and B as input, counts the occurrences of 'A' and 'B', and prints 'A' if the count of 'A' is higher, prints 'B' if the count of 'B' is higher, and takes no action if the counts are equal.

