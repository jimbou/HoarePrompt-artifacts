#State of the program right berfore the function call: stdin contains one input: a string
    return sys.stdin.readline().strip()
    #The program returns a string that was provided as input through stdin, with any leading or trailing whitespace removed.

#Overall this is what the function does:Reads a string from standard input, removes any leading or trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: func_1() returns a string that represents an integer
    return int(func_1())
    #The program returns an integer that is represented by the string returned by func_1().

#Overall this is what the function does:Converts a string representation of an integer returned by func_1() to an integer and returns it.

#State of the program right berfore the function call: func_1() returns a string of space-separated integers.
    return list(map(int, func_1().split()))
    #The program returns a list of integers, where each integer is a result of converting a string of space-separated integers returned by func_1() into an integer.

#Overall this is what the function does:The function takes no parameters and returns a list of integers. It converts a string of space-separated integers returned by func_1() into a list of integers, where each integer is a result of this conversion.

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
        
    #State: n is a positive integer, m is 0, x is a positive integer such that 1 <= x <= n, ans is a set containing all elements from 0 to n-1, r is an integer, c is a string, temp is a set containing all elements from 0 to n-1.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: *n is a positive integer, m is 0, x is a positive integer such that 1 <= x <= n, if 0 is in the set ans, then ans is a set containing all elements from 1 to n including n. Otherwise, no changes are made to the variables. r is an integer, c is a string, temp is a set containing all elements from 0 to n-1.
    print(len(ans))
    #This is printed: n (if 0 is in the set ans), or an unknown value (if 0 is not in the set ans)
    print(*ans)
    #This is printed: all elements from 1 to n including n if 0 is in the set ans, or the original elements of the set ans if 0 is not in the set ans

#Overall this is what the function does:This function generates a set of numbers from 1 to n (inclusive) based on the input parameters n, m, and x, and then prints the size of the set and its elements. If 0 is present in the set, it is replaced with n. The function's output depends on the presence of 0 in the set, resulting in either a set of numbers from 1 to n or the original set elements.

