#State of the program right berfore the function call: n is a positive integer, a is a list of n non-negative integers, and the sum of the elements in a is divisible by n.
    total_water = sum(a)
    if (total_water % n != 0) :
        return 'No'
        #The program returns the string 'No'.
    #State: *`n` is a positive integer, `a` is a list of `n` non-negative integers, `total_water` is equal to the sum of the elements in `a` and is divisible by `n`
    target = total_water // n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'No'
        
    #State: `n` is a positive integer, `a` is a list of `n` non-negative integers, `total_water` is equal to the sum of the elements in `a` and is divisible by `n`, `target` is equal to `total_water` divided by `n`, `container` is equal to the sum of all elements in `a` minus `n` times `target`, `water` is the last element in the list. If `container` is less than 0, the program returns the string 'No'. Otherwise, no changes are made.
    return 'Yes'
    #The program returns string 'Yes'

#Overall this is what the function does:Determines if it is possible to distribute water equally among 'n' containers given a list of 'n' non-negative integers representing the amount of water in each container. The function returns 'Yes' if the water can be distributed equally, and 'No' otherwise.

