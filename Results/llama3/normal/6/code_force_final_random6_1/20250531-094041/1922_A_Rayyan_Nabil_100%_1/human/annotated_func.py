#State of the program right berfore the function call: n is a positive integer, a, b, and c are strings of length n consisting of lowercase Latin letters.
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: `n` is a positive integer, `a`, `b`, `c` are strings of length `n` consisting of lowercase Latin letters. If there exists an `i` such that `a[i]` is not equal to `c[i]` and `b[i]` is not equal to `c[i]`, the program returns the string 'YES'. Otherwise, no action is taken.
    return 'NO'
    #The program returns the string 'NO'.

#Overall this is what the function does:This function compares three strings of equal length and returns 'YES' if it finds a position where both strings a and b differ from string c, otherwise it returns 'NO'.

#State of the program right berfore the function call: t is a positive integer, n is a positive integer, a, b, c are strings consisting of n lowercase Latin letters.
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        results.append(func_1(n, a, b, c))
        
    #State: t is 0, n is a positive integer equal to the input integer, a is a string consisting of n lowercase Latin letters, b is a string consisting of n lowercase Latin letters, c is a string consisting of n lowercase Latin letters, results is a list containing the results of func_1(n, a, b, c) for all iterations, stdin is empty
    for result in results:
        print(result)
        
    #State: `t` is 0, `n` is a positive integer equal to the input integer, `a` is a string consisting of `n` lowercase Latin letters, `b` is a string consisting of `n` lowercase Latin letters, `c` is a string consisting of `n` lowercase Latin letters, `results` is a list containing the results of `func_1(n, a, b, c)` for all iterations, `result` is the last result in the list, `stdin` is empty, and the last result in the list which is `result` is being printed.

#Overall this is what the function does:The function reads a series of inputs from the user, where each input consists of a positive integer `n` and three strings `a`, `b`, and `c` of length `n` containing lowercase Latin letters. It then calls another function `func_1` with these inputs and stores the results in a list. After all inputs have been processed, the function prints each result in the list. The function does not modify the input variables `t`, `n`, `a`, `b`, or `c`, and it does not perform any actions other than reading input, calling `func_1`, storing results, and printing output.

