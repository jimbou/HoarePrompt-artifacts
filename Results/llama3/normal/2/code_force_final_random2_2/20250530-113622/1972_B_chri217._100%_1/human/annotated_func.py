#State of the program right berfore the function call: stdin contains a sequence of inputs: first an integer t (1 <= t <= 100), then for each of the t test cases, first an integer n (1 <= n <= 100), then a string s of length n consisting of only "U" and "D" characters.
    t = int(sys.stdin.readline().strip())
    cases = []
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        
        s = sys.stdin.readline().strip()
        
        cases.append((n, s))
        
    #State: t is an integer between 1 and 100, cases is a list of t tuples, each tuple contains an integer n (1 <= n <= 100) and a string s of length n consisting of only "U" and "D" characters, _ is t-1, stdin is empty
    return cases
    #The program returns a list of t tuples, where t is an integer between 1 and 100. Each tuple contains an integer n, which is between 1 and 100, and a string s of length n consisting only of "U" and "D" characters.

#Overall this is what the function does:Reads input from stdin, parses it into a list of tuples, and returns the list. Each tuple contains an integer n and a string s of length n consisting only of "U" and "D" characters. The function does not perform any validation or processing on the input data beyond parsing it into the desired format.

#State of the program right berfore the function call: case is a list of two elements, the first element is an integer and the second element is a string consisting of 'U's and 'D's.
    ups = sum(1 for c in case[1] if c == 'U')
    return 'YES' if ups % 2 else 'NO'
    #The program returns 'YES' if the number of 'U's in the second element of the list `case` is odd, otherwise it returns 'NO'.

#Overall this is what the function does:This function determines whether the number of 'U's in the second element of the input list `case` is odd or even, returning 'YES' for odd counts and 'NO' for even counts.

