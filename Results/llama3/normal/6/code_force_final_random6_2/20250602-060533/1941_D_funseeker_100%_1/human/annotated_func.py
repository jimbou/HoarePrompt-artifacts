#State of the program right berfore the function call: stdin contains a string that needs to be read and stripped of leading/trailing whitespaces.
    return sys.stdin.readline().strip()
    #The program returns a string that was read from stdin and stripped of leading/trailing whitespaces.

#Overall this is what the function does:Reads a string from standard input, removes leading and trailing whitespaces, and returns the resulting string.

#State of the program right berfore the function call: func_1() returns a string that represents an integer.
    return int(func_1())
    #The program returns an integer that is represented by the string returned by func_1()

#Overall this is what the function does:The function takes no parameters and returns an integer that is represented by the string returned by func_1().

#State of the program right berfore the function call: func_1() returns a string of space-separated integers.
    return list(map(int, func_1().split()))
    #The program returns a list of integers that were originally returned by func_1() as a string of space-separated integers.

#Overall this is what the function does:The function accepts no parameters and returns a list of integers. It takes a string of space-separated integers returned by func_1(), splits it into individual integers, converts them to integers, and returns them as a list.

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
        
    #State: `n` is a positive integer, `m` is 0, `x` is a positive integer such that 1 <= `x` <= `n`, `ans` is a set containing all possible values of `(q + r) % n` and `(q - r) % n` for all `q` in the initial `ans`, `r` is an integer, `c` is a string.
    if (0 in ans) :
        ans.discard(0)
        ans.add(n)
    #State: *`n` is a positive integer, `m` is 0, `x` is a positive integer such that 1 <= `x` <= `n`, `ans` is a set containing all possible values of `(q + r) % n` and `(q - r) % n` for all `q` in the initial `ans`, except 0, plus n if 0 was in the initial `ans`, `r` is an integer, `c` is a string.
    print(len(ans))
    #This is printed: the number of unique values in the set ans
    print(*sorted(ans))
    #This is printed: a sorted list of unique values of (q + r) % n and (q - r) % n for all q in the initial ans, except 0, plus n if 0 was in the initial ans

#Overall this is what the function does:This function generates all possible values of (q + r) % n and (q - r) % n for a given set of initial values q, and prints the number of unique values and a sorted list of these values, excluding 0 and including n if 0 was in the initial set.

