#State of the program right berfore the function call: num is an integer such that 3 <= num <= 78.
    if (1 <= num <= 26) :
        return chr(num + 96)
        #The program returns a lowercase English letter that corresponds to the integer value of num, where num is between 1 and 26 (inclusive), and the ASCII value of the returned character is between 97 and 122 (inclusive).
    #State: *num is an integer such that 27 <= num <= 78

#Overall this is what the function does:Converts an integer to a lowercase English letter, but only if the integer is between 1 and 26 (inclusive), and returns the corresponding letter; otherwise, the function does not return a value.

