#State of the program right berfore the function call: n is a positive integer and a is a list of non-negative integers such that the sum of a is divisible by n.
    total_water = sum(a)
    if (total_water % n != 0) :
        return 'No'
        #The program returns string 'No'
    #State: *`n` is a positive integer, `a` is a list of non-negative integers such that the sum of `a` is divisible by `n`, `total_water` is the sum of `a` which is divisible by `n`, and `total_water` is divisible by `n`
    target = total_water // n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'No'
        
    #State: The program either returns the string 'No' if the calculated container value is negative at any point during the loop execution, or it continues execution until the end of the loop with the final values of `n`, `a`, `total_water`, `target`, and `container`, where `n` is a positive integer, `a` is a list of non-negative integers, `total_water` is the sum of `a` divisible by `n`, `target` is the quotient of `total_water` divided by `n`, and `container` is the final value after all iterations.
    return 'Yes'
    #The program returns 'Yes' indicating that the calculated container value was not negative at any point during the loop execution, and the final values of `n`, `a`, `total_water`, `target`, and `container` are preserved.

#Overall this is what the function does:Determines whether a list of non-negative integers can be distributed evenly among a specified number of containers, returning 'Yes' if possible and 'No' otherwise.

