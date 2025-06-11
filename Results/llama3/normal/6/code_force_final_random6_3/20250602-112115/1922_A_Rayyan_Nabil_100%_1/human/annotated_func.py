#State of the program right berfore the function call: n is a positive integer, a, b, and c are strings of lowercase Latin letters, and the length of a, b, and c is equal to n.
    for i in range(n):
        if a[i] != c[i] and b[i] != c[i]:
            return 'YES'
        
    #State: The loop finishes executing all iterations if and only if for all i in range(n), either a[i] is equal to c[i] or b[i] is equal to c[i].
    return 'NO'
    #The program returns string 'NO'

#Overall this is what the function does:This function compares strings a, b, and c of equal length n. It checks if there exists a character position i where both a[i] and b[i] are different from c[i]. If such a position is found, the function returns 'YES'. Otherwise, it returns 'NO', indicating that for all positions i, either a[i] or b[i] (or both) match c[i].

#State of the program right berfore the function call: t is a positive integer, n is a positive integer, a, b, c are strings of length n consisting of lowercase Latin letters.
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        
        a = input().strip()
        
        b = input().strip()
        
        c = input().strip()
        
        results.append(func_1(n, a, b, c))
        
    #State: t is at least t, _ is t-1, n is a positive integer, a is a string of length n consisting of lowercase Latin letters, b is a string of length n consisting of lowercase Latin letters, c is a string of length n consisting of lowercase Latin letters, results is a list containing t elements which are the results of func_1(n, a, b, c), stdin is empty
    for result in results:
        print(result)
        
    #State: `t` is at least `t`, `_` is `t-1`, `n` is a positive integer, `a` is a string of length `n` consisting of lowercase Latin letters, `b` is a string of length `n` consisting of lowercase Latin letters, `c` is a string of length `n` consisting of lowercase Latin letters, `results` is an empty list, `stdin` is empty, and the last element in the `results` list which is `result` has been printed.

#Overall this is what the function does:This function reads input from the user, processes it, and prints the results. It accepts no parameters and returns no value. The function reads a positive integer t, then for each iteration of t, it reads another positive integer n and three strings a, b, and c of length n consisting of lowercase Latin letters. It calls another function func_1 with these parameters and appends the result to a list. After processing all iterations, it prints each result from the list. The function modifies the state of the program by emptying the input buffer and printing the results.

