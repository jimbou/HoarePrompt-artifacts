#State of the program right berfore the function call: stdin contains multiple lines of input: the first line contains a positive integer t, followed by t pairs of lines where the first line of each pair contains a positive integer n, and the second line of each pair contains a string s of length n consisting only of "U" and "D".
    t = int(sys.stdin.readline().strip())
    cases = []
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        
        s = sys.stdin.readline().strip()
        
        cases.append((n, s))
        
    #State: t is a positive integer, cases is a list of t pairs where each pair contains a positive integer n and a string s of length n consisting only of "U" and "D", _ is t-1, stdin is empty
    return cases
    #The program returns a list of t pairs, where each pair contains a positive integer n and a string s of length n consisting only of "U" and "D".

#Overall this is what the function does:Reads input from standard input, where the first line contains a positive integer t, followed by t pairs of lines, and returns a list of t pairs, where each pair contains a positive integer n and a string s of length n consisting only of "U" and "D".

#State of the program right berfore the function call: case is a list of two elements, the first element is a positive integer and the second element is a string of length equal to the first element, containing only 'U' and 'D' characters.
    ups = sum(1 for c in case[1] if c == 'U')
    return 'YES' if ups % 2 else 'NO'
    #The program returns 'YES' if the number of 'U' characters in the second element of `case` is odd, otherwise it returns 'NO'.

#Overall this is what the function does:Determines whether the number of 'U' characters in a given string is odd or even, returning 'YES' for odd counts and 'NO' for even counts.

