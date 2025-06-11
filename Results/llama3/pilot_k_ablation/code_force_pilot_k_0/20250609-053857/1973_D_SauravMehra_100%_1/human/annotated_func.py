#State of the program right berfore the function call: tar is a positive integer, k is a positive integer, n is a positive integer such that k <= n.
    it = 0
    ind = 0
    while ind < n and it < k:
        print(f'? {ind + 1} {tar}')
        
        x = int(input())
        
        if x == n + 1:
            return False
        
        ind = x
        
        it += 1
        
    #State: it is a positive integer, ind is a positive integer, tar is a positive integer, k is a positive integer, n is a positive integer such that k <= n, it is a positive integer, ind is a positive integer.
    return ind == n and it == k
    #The program returns a boolean value indicating whether the conditions 'ind is equal to n' and 'it is equal to k' are both true, where 'ind' and 'n' are positive integers, and 'it' and 'k' are positive integers such that k is less than or equal to n.

#Overall this is what the function does:This function determines whether a target value 'tar' can be reached by iteratively guessing a value 'ind' up to 'k' times, where 'ind' is a positive integer less than or equal to 'n'. It returns True if 'ind' equals 'n' and the number of iterations 'it' equals 'k', and False otherwise. The function also handles the case where the user inputs 'n + 1', in which case it immediately returns False.

