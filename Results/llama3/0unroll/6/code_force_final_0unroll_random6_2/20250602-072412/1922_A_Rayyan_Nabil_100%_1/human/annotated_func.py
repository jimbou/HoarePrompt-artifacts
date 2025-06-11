#State of the program right berfore the function call: n is a positive integer, a, b, and c are strings of length n consisting of lowercase Latin letters.
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: The loop will return 'YES' if there exists at least one position i where a[i] and b[i] are both different from c[i]. If no such position is found after checking all n positions, the loop will finish without returning anything, leaving the state unchanged.
    return 'NO'
    #The program returns 'NO'

#Overall this is what the function does:The function compares two strings `a` and `b` of length `n` with a third string `c` of the same length, and returns 'YES' if there exists at least one position where both `a` and `b` differ from `c`, otherwise it returns 'NO'.

#State of the program right berfore the function call: t is a positive integer, n is a positive integer, a, b, c are strings of lowercase Latin letters, and the length of a, b, c is equal to n.
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        results.append(func_1(n, a, b, c))
        
    #State: t is an integer, n is a positive integer, a, b, c are strings of lowercase Latin letters, and the length of a, b, c is equal to n, results is a list of t elements, each element is the result of func_1(n, a, b, c) for each iteration of the loop, stdin is empty.
    for result in results:
        print(result)
        
    #State: Output State: The output state after the loop executes all the iterations is that the variable "result" has taken on the value of each element in the list "results" in sequence, and the print function has been called for each element in "results", printing each result to the console. The values of the other variables (t, n, a, b, c, results, stdin) remain unchanged.

#Overall this is what the function does:The function accepts a positive integer t, which represents the number of test cases. For each test case, it accepts a positive integer n and three strings a, b, and c, each of length n, consisting of lowercase Latin letters. The function then appends the result of func_1(n, a, b, c) to the results list for each test case. Finally, it prints each result in the results list to the console. The function does not modify the input variables t, n, a, b, c, or the stdin.

