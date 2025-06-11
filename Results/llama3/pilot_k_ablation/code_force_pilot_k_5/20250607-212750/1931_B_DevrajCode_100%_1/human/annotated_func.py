#State of the program right berfore the function call: n is a positive integer and a is a list of n non-negative integers such that the sum of a is divisible by n.
    total_water = sum(a)
    target = total_water // n
    if (total_water % n != 0) :
        return 'NO'
        #The program returns the string 'NO'.
    #State: *n is a positive integer, a is a list of n non-negative integers, total_water is the sum of a, target is the sum of a divided by n, and total_water is divisible by n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'NO'
        
    #State: `n` is a positive integer, `a` is a list of `n` non-negative integers, `total_water` is the sum of `a`, `target` is the sum of `a` divided by `n`, and `container` is 0.
    return 'YES'
    #The program returns the string 'YES'.

#Overall this is what the function does:Determines if it is possible to distribute water evenly among n containers, given a list of n non-negative integers representing the amount of water in each container, and returns 'YES' if possible, 'NO' otherwise.

