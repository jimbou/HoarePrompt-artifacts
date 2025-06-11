#State of the program right berfore the function call: stdin contains a string
    return sys.stdin.readline().strip()
    #The program returns a string that is read from the standard input (stdin), with leading and trailing whitespace removed.

#Overall this is what the function does:Reads a line of input from the standard input (stdin) and returns the input string with leading and trailing whitespace removed.

#State of the program right berfore the function call: func_1() returns a string that can be converted to an integer
    return int(func_1())
    #The program returns an integer that is converted from the string returned by func_1()

#Overall this is what the function does:Converts the string returned by func_1() to an integer and returns it.

#State of the program right berfore the function call: func_1() returns a string of space-separated integers
    return list(map(int, func_1().split()))
    #The program returns a list of integers that were originally returned by func_1() as a string of space-separated integers.

#Overall this is what the function does:The function takes no parameters and returns a list of integers. It converts a string of space-separated integers returned by func_1() into a list of integers.

#State of the program right berfore the function call: n is a positive integer, m is a non-negative integer, and x is a positive integer such that 1 <= x <= n.
    n, m, x = func_3()
    ans = {x}
    for _ in range(m):
        r, c = func_1().split()
        
        r = int(r)
        
        temp = set()
        
        for q in ans:
            if c == '0' or c == '?':
                temp.add((q + r) % n)
            if c == '1' or c == '?':
                temp.add((q - r) % n)
        
        ans = temp
        
    #State: Output State: n is a positive integer, m is 0, x is a positive integer such that 1 <= x <= n, ans is a set containing all possible values of x after m iterations of the loop.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: *n is a positive integer, m is 0, x is a positive integer such that 1 <= x <= n, ans is a set containing all possible values of x after m iterations of the loop. If 0 is in ans, then ans includes n but does not include 0.
    print(len(ans))
    #This is printed: 1
    print(*sorted(ans))
    #This is printed: 1 2 3 ... n (where n is the value of n)

#Overall this is what the function does:This function calculates and returns the number of possible values of x after m iterations of a loop, where x is a positive integer between 1 and n (inclusive), and m is a non-negative integer. The function also prints the sorted list of possible values of x. If 0 is a possible value, it is replaced with n. The function assumes that the input values n, m, and x are obtained from another function func_3(), and that func_1() is used to generate random values for the loop iterations.

