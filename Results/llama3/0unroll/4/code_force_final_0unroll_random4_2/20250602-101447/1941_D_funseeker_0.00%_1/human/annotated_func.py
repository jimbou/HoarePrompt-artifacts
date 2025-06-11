#State of the program right berfore the function call: stdin contains a string
    return sys.stdin.readline().strip()
    #The program returns the string from stdin, stripped of leading and trailing whitespace.

#Overall this is what the function does:Reads a line of input from standard input, removes leading and trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: func_1() returns a string that can be converted to an integer
    return int(func_1())
    #The program returns an integer converted from a string returned by func_1()

#Overall this is what the function does:The function takes no parameters and returns an integer that is converted from a string returned by another function, func_1().

#State of the program right berfore the function call: func_1() returns a string of space-separated integers
    return list(map(int, func_1().split()))
    #The program returns a list of integers, where each integer is a result of converting a string of space-separated integers returned by func_1() into an integer.

#Overall this is what the function does:This function takes no parameters and returns a list of integers. It converts a string of space-separated integers returned by another function, func_1(), into a list of integers, where each integer is a result of the conversion. The function does not modify any input variables, as it does not accept any. The final state of the program is that it returns a list of integers, which are the converted results from the string returned by func_1().

#State of the program right berfore the function call: n is a positive integer, m is a non-negative integer, x is a positive integer such that 1 <= x <= n.
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
        
    #State: Output State: n is a positive integer, m is a non-negative integer, x is a positive integer such that 1 <= x <= n, ans is a set containing all possible values of (x + r1 + r2 + ... + rm) % n and (x - r1 - r2 - ... - rm) % n, where ri is the value of r in the ith iteration of the loop.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: n is a positive integer, m is a non-negative integer, x is a positive integer such that 1 <= x <= n, ans is a set containing all possible values of (x + r1 + r2 + ... + rm) % n and (x - r1 - r2 - ... - rm) % n, where ri is the value of r in the ith iteration of the loop. If 0 is in the set ans, then the set ans contains n.
    print(len(ans))
    #This is printed: the number of unique values of (x + r1 + r2 + ... + rm) % n and (x - r1 - r2 - ... - rm) % n in the range 0 <= (x + r1 + r2 + ... + rm) % n <= n-1 and 0 <= (x - r1 - r2 - ... - rm) % n <= n-1, plus 1 if 0 is in the set ans
    print(*ans)
    #This is printed: all unique values of (x + r1 + r2 + ... + rm) % n and (x - r1 - r2 - ... - rm) % n, where ri is the value of r in the ith iteration of the loop, and if 0 is in the set, then n

#Overall this is what the function does:This function calculates and prints the number of unique values and the values themselves of the expression (x + r1 + r2 + ... + rm) % n and (x - r1 - r2 - ... - rm) % n, where x is a positive integer, n is a positive integer, m is a non-negative integer, and ri is a value obtained from an external function. If the result set contains 0, it is replaced with n. The function takes no arguments and returns no value, but instead prints the count and the values of the unique results.

