#State of the program right berfore the function call: n is a positive integer, a is a list of non-negative integers, the length of a is n, and the sum of a is divisible by n.
    total_water = sum(a)
    target = total_water // n
    if (total_water % n != 0) :
        return 'NO'
        #The program returns the string 'NO'
    #State: *n is a positive integer, a is a list of non-negative integers, the length of a is n, total_water is the sum of a, target is the integer division of total_water by n, and total_water is divisible by n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'NO'
        
    #State: `n` is a positive integer, `a` is a list of non-negative integers, the length of `a` is `n`, `total_water` is the sum of `a`, `target` is the integer division of `total_water` by `n`, `total_water` is divisible by `n`, and `container` is 0.
    return 'YES'
    #The program returns string 'YES'

#Overall this is what the function does:Functionality: This function determines whether it is possible to distribute water evenly among 'n' containers, where 'n' is a positive integer and the water is represented by a list of non-negative integers 'a' of length 'n'. The function returns 'YES' if the water can be distributed evenly and 'NO' otherwise.

