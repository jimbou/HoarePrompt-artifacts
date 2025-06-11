#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a positive integer t. Each of the following lines contains a positive integer n, followed by a string s of length n containing only "U" and "D".
    t = int(sys.stdin.readline().strip())
    cases = []
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        
        s = sys.stdin.readline().strip()
        
        cases.append((n, s))
        
    #State: Output State: t is a positive integer, cases is a list of t tuples, each containing a positive integer n and a string s of length n containing only "U" and "D", stdin is empty.
    return cases
    #The program returns a list of t tuples, where t is a positive integer. Each tuple contains a positive integer n and a string s of length n, consisting only of "U" and "D" characters.

#Overall this is what the function does:Reads input from standard input, parses it into a list of tuples, and returns the list. Each tuple contains a positive integer n and a string s of length n, consisting only of "U" and "D" characters. The function consumes all input from standard input, leaving it empty.

#State of the program right berfore the function call: case is a list of two elements, the first element is a positive integer and the second element is a string of length equal to the first element, consisting only of 'U' and 'D' characters.
    ups = sum(1 for c in case[1] if c == 'U')
    return 'YES' if ups % 2 else 'NO'
    #The program returns 'YES' if the number of 'U' characters in the second element of the `case` list is odd, otherwise it returns 'NO'.

#Overall this is what the function does:Determines whether the number of 'U' characters in a given string is odd or even, returning 'YES' for odd counts and 'NO' for even counts.

