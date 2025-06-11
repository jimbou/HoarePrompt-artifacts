#State of the program right berfore the function call: n is a positive integer, a is a list of non-negative integers of length n, the sum of the elements in a is divisible by n.
    total_water = sum(a)
    if (total_water % n != 0) :
        return 'No'
        #The program returns the string 'No'
    #State: *`n` is a positive integer, `a` is a list of non-negative integers of length `n`, `total_water` is the sum of the elements in `a` which is divisible by `n`, and `total_water` is divisible by `n`
    target = total_water // n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'No'
        
    #State: Output State: The container is 0, and the function returns 'No'.
    return 'Yes'
    #The program returns 'Yes'

#Overall this is what the function does:Determines whether a given list of non-negative integers can be distributed evenly among a specified number of containers, returning 'Yes' if possible and 'No' otherwise.

