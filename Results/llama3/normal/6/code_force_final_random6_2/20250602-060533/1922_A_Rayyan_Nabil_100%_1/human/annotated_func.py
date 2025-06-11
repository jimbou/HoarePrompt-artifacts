#State of the program right berfore the function call: n is a positive integer, a, b, and c are strings of length n, consisting of lowercase Latin letters.
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: n is a positive integer, a, b, and c are strings of length n, consisting of lowercase Latin letters, i is n. If there exists an index j such that a[j] is not equal to c[j] and b[j] is not equal to c[j], the program returns the string 'YES'. Otherwise, no action is taken.
    return 'NO'
    #The program returns the string 'NO'.

#Overall this is what the function does:This function compares three strings of equal length, 'a', 'b', and 'c', and returns 'YES' if there exists at least one position where both 'a' and 'b' differ from 'c', otherwise it returns 'NO'.

#State of the program right berfore the function call: t is a positive integer, n is a positive integer, a, b, c are strings consisting of n lowercase Latin letters.
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        results.append(func_1(n, a, b, c))
        
    #State: t is 0, n is a positive integer equal to its original value plus the integer value of the input, a, b, c are strings consisting of n lowercase Latin letters, results is a list containing t elements: each element is the return value of func_1(n, a, b, c) with the values of n, a, b, c at each iteration, stdin is empty, _ is t-1
    for result in results:
        print(result)
        
    #State: `t` is equal to the length of `results`, `n` is a positive integer equal to its original value plus the integer value of the input, `a`, `b`, `c` are strings consisting of `n` lowercase Latin letters, `results` is a list containing `t` elements: each element is the return value of `func_1(n, a, b, c)` with the values of `n`, `a`, `b`, `c` at each iteration, `stdin` is empty, `_` is `t-1`, and all elements in `results` have been printed.

#Overall this is what the function does:The function reads input from the user, processes it, and prints the results. It accepts a positive integer `t` and `t` sets of input, each consisting of a positive integer `n` and three strings `a`, `b`, and `c` of length `n`. The function calls another function `func_1` with these inputs and stores the results in a list. After processing all inputs, the function prints each result in the list. The final state of the program is that all input has been processed, the results have been printed, and the input buffer is empty.

