#State of the program right berfore the function call: stdin contains a string that is expected to be read and stripped of leading/trailing whitespaces.
    return sys.stdin.readline().strip()
    #The program returns a string that was read from stdin and stripped of leading/trailing whitespaces.

#Overall this is what the function does:Reads a line of input from standard input (stdin), removes leading and trailing whitespace characters, and returns the resulting string.

#State of the program right berfore the function call: func_1() returns a string that represents an integer.
    return int(func_1())
    #The program returns an integer that is represented by the string returned by func_1()

#Overall this is what the function does:Converts a string representation of an integer returned by func_1() to an integer and returns it.

#State of the program right berfore the function call: func_1() returns a string of space-separated integers
    return list(map(int, func_1().split()))
    #The program returns a list of integers that were originally space-separated strings returned by func_1()

#Overall this is what the function does:Converts a string of space-separated integers returned by func_1() into a list of integers and returns it.

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
        
    #State: n is a positive integer, m is a non-negative integer, x is a positive integer such that 1 <= x <= n, ans is a set containing all possible remainders of (each element in the initial ans + r) divided by n if c is '0' or '1', or all possible remainders of (each element in the initial ans + r) divided by n and all possible remainders of (each element in the initial ans - r) divided by n if c is '?', otherwise ans is an empty set, _ is m, r is an integer, c is either '0', '1', '?' or another character, q is undefined, temp is an empty set.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: *n is a positive integer, m is a non-negative integer, x is a positive integer such that 1 <= x <= n, r is an integer, c is either '0', '1', '?' or another character, q is undefined. If 0 is in the set ans, then ans is a set containing n. Otherwise, no change is made to ans.
    print(len(ans))
    #This is printed: 1 (if 0 is in the set ans) or the original length of ans (if 0 is not in the set ans)
    print(*sorted(ans))
    #This is printed: the elements of the set ans in sorted order (either a single element n if 0 is in ans, or the original elements of ans in sorted order if 0 is not in ans)

#Overall this is what the function does:This function generates all possible remainders of a sequence of operations on an initial value x, where the operations are either addition or subtraction of a value r, modulo n. The sequence of operations is determined by a string of characters, where '0' indicates addition, '1' indicates subtraction, and '?' indicates both addition and subtraction. The function then prints the number of unique remainders and the remainders themselves in sorted order. If the remainder 0 is present, it is replaced with n.

