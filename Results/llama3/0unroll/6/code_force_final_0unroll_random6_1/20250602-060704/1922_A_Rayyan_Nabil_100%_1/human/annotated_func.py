#State of the program right berfore the function call: n is a positive integer, a, b, and c are strings of length n consisting of lowercase Latin letters.
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: The loop will return 'YES' if there exists at least one position i where a[i] and b[i] are both different from c[i]. If no such position is found after checking all n positions, the loop will finish without returning anything, and the state of the variables a, b, and c will remain unchanged.
    return 'NO'
    #The program returns 'NO' regardless of the values of variables a, b, and c.

#Overall this is what the function does:This function checks if there exists at least one position where two input strings (a and b) are both different from a third input string (c). If such a position is found, it returns 'YES'. If no such position is found after checking all positions, it returns 'NO'. The function does not modify the input strings.

#State of the program right berfore the function call: t is a positive integer, n is a positive integer, a, b, c are strings of lowercase Latin letters of length n.
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        results.append(func_1(n, a, b, c))
        
    #State: Output State: t is an integer, n is a positive integer, a, b, c are strings of lowercase Latin letters of length n, results is a list of t elements, each element is the result of func_1(n, a, b, c) for the corresponding iteration, stdin is empty.
    for result in results:
        print(result)
        
    #State: Output State: The output state after the loop executes all the iterations is that the results list is empty, and the values of t, n, a, b, c, and stdin remain unchanged.

#Overall this is what the function does:The function accepts four parameters: a positive integer `n` and three strings `a`, `b`, and `c` of length `n`, each consisting of lowercase Latin letters. It returns a result based on these inputs, which is appended to a list of results. The function is called `t` times, where `t` is a positive integer, and each call processes a new set of inputs. The function's purpose is to process the input strings `a`, `b`, and `c` of length `n` and produce a result, which is collected in a list and printed out. The final state of the program is that the list of results is empty, and the input values are unchanged.

