#State of the program right berfore the function call: n is a positive integer, a is a list of non-negative integers, the length of a is equal to n, and the sum of a is divisible by n.
    total_water = sum(a)
    target = total_water // n
    if (total_water % n != 0) :
        return 'NO'
        #The program returns the string 'NO'.
    #State: *n is a positive integer, a is a list of non-negative integers, the length of a is equal to n, total_water is the sum of a, target is the integer division of total_water by n, and total_water is divisible by n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'NO'
        
    #State: `n` is a positive integer, `a` is a list of non-negative integers, the length of `a` is equal to `n`, `total_water` is the sum of `a`, `target` is the integer division of `total_water` by `n`, `total_water` is divisible by `n`, and `container` is 0.
    return 'YES'
    #The program returns the string 'YES'.

#Overall this is what the function does:Determines whether it is possible to distribute water evenly among n containers, given a list of non-negative integers representing the initial water levels in each container. The function returns 'YES' if the water can be distributed evenly, and 'NO' otherwise.

