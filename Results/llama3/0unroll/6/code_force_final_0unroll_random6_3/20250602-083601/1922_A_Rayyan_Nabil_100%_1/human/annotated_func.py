#State of the program right berfore the function call: n is a positive integer, a, b, and c are strings of lowercase Latin letters, and the length of a, b, and c is equal to n.
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: If there exists at least one index i such that a[i] is not equal to c[i] and b[i] is not equal to c[i], then the output state is 'YES'. Otherwise, the output state is the initial state with no changes.
    return 'NO'
    #The program returns 'NO'

#Overall this is what the function does:This function compares three strings (a, b, and c) of equal length (n) and returns 'YES' if it finds at least one position where both a and b differ from c, otherwise it returns 'NO'. The function does not modify the input strings.

#State of the program right berfore the function call: t is a positive integer, n is a positive integer, a, b, and c are strings of length n consisting of lowercase Latin letters.
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        results.append(func_1(n, a, b, c))
        
    #State: Output State: t is a positive integer equal to the input value, n is a positive integer, a, b, and c are strings of length n consisting of lowercase Latin letters, results is a list of t elements, each element being the output of func_1(n, a, b, c) for the corresponding iteration of the loop.
    for result in results:
        print(result)
        
    #State: Output State: The loop has executed all iterations, printing each element of the results list. The values of t, n, a, b, and c remain unchanged as they are not affected by the loop head and body. The output state is the same as the initial state, with the only difference being that the elements of the results list have been printed to the console.

#Overall this is what the function does:This function reads input from the user, processes it, and prints the results. It accepts a positive integer t, which represents the number of test cases, and for each test case, it reads a positive integer n and three strings a, b, and c of length n consisting of lowercase Latin letters. The function then calls another function, func_1, with these inputs and appends the result to a list. After processing all test cases, it prints each element of the results list. The function does not modify the input values and only produces output based on the func_1 function calls.

