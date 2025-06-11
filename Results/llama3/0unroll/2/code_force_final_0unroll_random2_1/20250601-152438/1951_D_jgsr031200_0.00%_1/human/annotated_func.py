#State of the program right berfore the function call: n and k are positive integers.
    if (n == k) :
        print('YES')
        #This is printed: YES
        print(1)
        #This is printed: 1
        print(1)
        #This is printed: 1
        return
        #The program returns nothing because the return statement is empty, and the current state of the program is that 'YES' has been printed, 1 has been printed twice, and n and k are equal positive integers.
    #State: n and k are positive integers, and n is not equal to k
    if (n < k) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing, as there is no value or variable specified in the return statement. The values of n and k remain unchanged, with n being a positive integer less than k, and 'NO' is still being printed.
    #State: n and k are positive integers, n is not equal to k, and n is larger than or equal to k
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: Output State: n is 0, k is a positive integer, costs is a list containing two integers: n - k + 1 and 1, h is n + k - 1.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print(2)
        #This is printed: 2
        print('YES')
        #This is printed: YES
        print(*costs)
        #This is printed: -k + 1, 1 (where k is a positive integer)
    #State: n is 0, k is a positive integer, costs is a list containing two integers: n - k + 1 and 1, h is n + k - 1. If h is less than k, 'NO' is printed and the current value of h is -1 + k. If h is larger than or equal to k, 'YES' is printed, and the elements of the costs list which are -k+1 and 1 are printed.

#Overall this is what the function does:This function determines whether it is possible to reach a target value `k` by subtracting two specific costs from a given value `n`. If `n` is equal to `k`, it prints 'YES' and the cost 1 twice. If `n` is less than `k`, it prints 'NO'. If `n` is greater than or equal to `k`, it calculates the maximum number of times each cost can be subtracted from `n` without exceeding `k`, and prints 'YES' along with the costs if the total number of subtractions is greater than or equal to `k`, or 'NO' otherwise.

