#State of the program right berfore the function call: s is a string of length n (1 <= n <= 100) consisting of characters 'U' and 'D'.
    num_up = s.count('U')
    if (num_up % 2 == 1) :
        return 'YES'
        #The program returns the string 'YES'
    else :
        return 'NO'
        #The program returns the string 'NO'

#Overall this is what the function does:Determines whether the number of 'U's in a given string is odd or even, returning 'YES' if odd and 'NO' if even.

