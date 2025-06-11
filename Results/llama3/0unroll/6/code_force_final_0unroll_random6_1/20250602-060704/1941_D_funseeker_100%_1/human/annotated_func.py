#State of the program right berfore the function call: stdin contains one input: a string
    return sys.stdin.readline().strip()
    #The program returns a string that was provided as input from stdin, with any leading or trailing whitespace removed.

#Overall this is what the function does:Reads a string from standard input, removes any leading or trailing whitespace, and returns the resulting string.

#State of the program right berfore the function call: func_1() returns a string that represents an integer
    return int(func_1())
    #The program returns an integer that is represented by the string returned by func_1()

#Overall this is what the function does:Converts a string representation of an integer returned by func_1() to an integer and returns it.

#State of the program right berfore the function call: func_1() returns a string of space-separated integers.
    return list(map(int, func_1().split()))
    #The program returns a list of integers that were originally returned by func_1() as a string of space-separated integers.

#Overall this is what the function does:The function takes no parameters and returns a list of integers. It converts a string of space-separated integers returned by func_1() into a list of integers. The function does not modify any external state or perform any side effects, solely focusing on the conversion and return of the integer list.

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
        
    #State: Output State: n is a positive integer, m is a non-negative integer, x is a positive integer such that 1 <= x <= n, ans is a set containing all possible values of x after m iterations of the loop.
    #
    #In natural language, the output state is: The value of n and m remains unchanged, but the value of x has been transformed into a set of all possible values that x can take after m iterations of the loop, where in each iteration, x is either incremented or decremented by a random value r (obtained from func_1()) modulo n.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: *n is a positive integer, m is a non-negative integer, x is a positive integer such that 1 <= x <= n, ans is a set containing all possible values of x after m iterations of the loop. If 0 is in ans, then ans includes n but does not include 0. Otherwise, no additional information is available about ans.
    print(len(ans))
    #This is printed: the number of elements in the set ans (which is at most n)
    print(*sorted(ans))
    #This is printed: a sequence of positive integers from 1 to n, possibly including n, in ascending order, with the exact elements depending on the values of x and m

#Overall this is what the function does:This function generates a set of all possible values that a given positive integer x can take after a specified number of iterations m, where in each iteration, x is either incremented or decremented by a random value r modulo n. The function then prints the number of unique possible values and the sorted sequence of these values, excluding 0 and including n if 0 is present.

