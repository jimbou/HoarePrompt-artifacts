#State of the program right berfore the function call: n and k are positive integers.
    if (n == k) :
        print('YES')
        #This is printed: YES
        print(1)
        #This is printed: 1
        print(1)
        #This is printed: 1
        return
        #The program returns nothing, as the return statement is empty. The values of n and k remain unchanged, still being equal to each other. The previously printed values 'YES', 1, and 1 remain printed.
    #State: *n and k are positive integers, and n is not equal to k
    if (n < k) :
        print('NO')
        #This is printed: NO
        return
        #The program returns nothing, as the return statement is empty. The values of n and k remain unchanged, with n being less than k. The program also does not print anything, as the 'NO' print statement is not executed due to the return statement.
    #State: *n and k are positive integers, n is not equal to k, and n is larger than or equal to k
    costs = [n - k + 1, 1]
    h = 0
    for i in costs:
        curr = n // i
        
        h += curr
        
        n -= i * curr
        
    #State: Output State: n is 0, k is a positive integer, n is not equal to k, n is smaller than k, costs is a list containing two elements: n - k + 1 and 1, h is a positive integer.
    if (h < k) :
        print('NO')
        #This is printed: NO
    else :
        print(2)
        #This is printed: 2
        print('YES')
        #This is printed: YES
        print(*costs)
        #This is printed: [n - k + 1] (where n - k + 1 is a negative integer), 1
    #State: n is 0, k is a positive integer, n is not equal to k, n is smaller than k, costs is a list containing two elements: n - k + 1 and 1, h is a positive integer. If h is less than k, 'NO' is printed. If h is larger than or equal to k, 'YES' is printed along with n - k + 1 and 1.

#Overall this is what the function does:This function determines whether it is possible to make a certain number of items (k) using a given number of units (n), with the option to use two different unit sizes (n - k + 1 and 1). If n is equal to k, it prints 'YES' and the unit sizes 1 and 1. If n is less than k, it prints 'NO'. If n is greater than or equal to k, it calculates the number of units of each size needed to make k items and prints 'YES' along with the unit sizes if the total number of units is greater than or equal to k, otherwise it prints 'NO'. The function does not return any values, but instead prints the results directly.

