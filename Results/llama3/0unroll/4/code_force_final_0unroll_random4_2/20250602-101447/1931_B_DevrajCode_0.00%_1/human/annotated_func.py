#State of the program right berfore the function call: n is a positive integer, a is a list of n non-negative integers, and the sum of a is divisible by n.
    total_water = sum(a)
    if (total_water % n != 0) :
        return 'No'
        #The program returns the string 'No'.
    #State: *`n` is a positive integer, `a` is a list of `n` non-negative integers, `total_water` is the sum of `a`, the sum of `a` is divisible by `n`, and `total_water` is divisible by `n`
    target = total_water // n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'No'
        
    #State: container is 0, and the function returns 'Yes'
    return 'Yes'
    #The program returns 'Yes' and the variable container remains 0.

#Overall this is what the function does:Determines if it is possible to distribute water evenly among n containers, given a list of n non-negative integers representing the initial water levels in each container. The function returns 'Yes' if the water can be distributed evenly and 'No' otherwise.

