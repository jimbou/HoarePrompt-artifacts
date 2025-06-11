#State of the program right berfore the function call: stdin contains a string
    return sys.stdin.readline().strip()
    #The program returns a string that is read from the standard input (stdin) with any leading or trailing whitespace removed.

#Overall this is what the function does:Reads a line of input from the standard input (stdin), removes any leading or trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: func_1() returns a string that can be converted to an integer.
    return int(func_1())
    #The program returns an integer that is converted from the string returned by func_1()

#Overall this is what the function does:The function accepts no parameters and returns an integer that is converted from the string returned by func_1().

#State of the program right berfore the function call: func_1() returns a string of space-separated integers
    return list(map(int, func_1().split()))
    #The program returns a list of integers, where each integer is a result of converting a string of space-separated integers returned by func_1() into an integer.

#Overall this is what the function does:This function takes no parameters and returns a list of integers. It converts a string of space-separated integers returned by another function, func_1(), into a list of integers. The function does not modify any input variables as it does not accept any parameters. Upon conclusion, the program's state is that it has returned a list of integers, where each integer is a result of the conversion process.

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
        
    #State: Output State: n is a positive integer, m is a non-negative integer, x is a positive integer such that 1 <= x <= n, ans is a set containing all possible values of (x + r1 + r2 + ... + rm) % n and (x - r1 - r2 - ... - rm) % n, where ri is the result of func_1() for each iteration of the loop.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: n is a positive integer, m is a non-negative integer, x is a positive integer such that 1 <= x <= n, ans is a set containing all possible values of (x + r1 + r2 + ... + rm) % n and (x - r1 - r2 - ... - rm) % n, where ri is the result of func_1() for each iteration of the loop. If 0 is in ans, then 0 is excluded from ans and n is included in ans. Otherwise, ans remains unchanged.
    print(len(ans))
    #This is printed: the number of unique possible values of (x + r1 + r2 + ... + rm) % n and (x - r1 - r2 - ... - rm) % n after the exclusion of 0 and inclusion of n if necessary
    print(*sorted(ans))
    #This is printed: the unique values in ans in ascending order (where ans is the set containing all possible values of (x + r1 + r2 + ... + rm) % n and (x - r1 - r2 - ... - rm) % n, with 0 excluded and n included if 0 is present)

#Overall this is what the function does:This function generates and returns all possible values of (x + r1 + r2 + ... + rm) % n and (x - r1 - r2 - ... - rm) % n, where ri is the result of func_1() for each iteration of the loop, given a positive integer n, a non-negative integer m, and a positive integer x such that 1 <= x <= n. It then prints the number of unique possible values and the unique values in ascending order, excluding 0 and including n if 0 is present.

