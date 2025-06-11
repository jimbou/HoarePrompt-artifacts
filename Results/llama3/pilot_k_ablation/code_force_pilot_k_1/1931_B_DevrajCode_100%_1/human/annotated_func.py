#State of the program right berfore the function call: n is a positive integer, a is a list of n non-negative integers, and the sum of the elements in a is divisible by n.
    total_water = sum(a)
    target = total_water // n
    if (total_water % n != 0) :
        return 'NO'
        #The program returns the string 'NO'.
    #State: *n is a positive integer, a is a list of n non-negative integers, total_water is the sum of the elements in a, target is the sum of the elements in a divided by n, and total_water is divisible by n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'NO'
        
    #State: `n` is a positive integer, `a` is a list of `n` non-negative integers, `total_water` is the sum of the elements in `a`, `target` is the sum of the elements in `a` divided by `n`, `total_water` is divisible by `n`, and `container` is the sum of the differences between each element in `a` and `target`. If the loop completes without returning 'NO', then `container` is not less than 0. If `a` is empty, the loop does not execute and `container` remains 0.
    return 'YES'
    #The program returns the string 'YES'

#Overall this is what the function does:Determines if it's possible to distribute water evenly among containers.

