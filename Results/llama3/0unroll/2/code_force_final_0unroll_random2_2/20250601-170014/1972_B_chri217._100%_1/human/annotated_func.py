#State of the program right berfore the function call: stdin contains multiple lines of input: the first line contains a positive integer t, and for each test case, the first line contains a positive integer n and the second line contains a string s of length n consisting only of "U" and "D".
    t = int(sys.stdin.readline().strip())
    cases = []
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        
        s = sys.stdin.readline().strip()
        
        cases.append((n, s))
        
    #State: t is a positive integer, cases is a list of tuples where each tuple contains a positive integer n and a string s of length n consisting only of "U" and "D", stdin is empty.
    return cases
    #The program returns a list of tuples where each tuple contains a positive integer n and a string s of length n consisting only of "U" and "D".

#Overall this is what the function does:Reads input from stdin, parses it into a list of test cases, and returns the list. Each test case is a tuple containing a positive integer n and a string s of length n consisting only of "U" and "D".

#State of the program right berfore the function call: case is a list of two elements, the first element is a positive integer and the second element is a string of length equal to the first element, containing only 'U' and 'D' characters.
    ups = sum(1 for c in case[1] if c == 'U')
    return 'YES' if ups % 2 else 'NO'
    #The program returns 'YES' if ups is an odd integer less than or equal to the first element of the case list, otherwise it returns 'NO'.

#Overall this is what the function does:This function determines whether a given case, consisting of a positive integer and a string of 'U' and 'D' characters of equal length, meets a specific condition. It counts the number of 'U' characters in the string and returns 'YES' if this count is an odd integer less than or equal to the given positive integer, otherwise it returns 'NO'.

