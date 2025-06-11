#State of the program right berfore the function call: n is a positive integer, a is a list of non-negative integers, the sum of a is divisible by n, and 1 <= n <= 2 * 10^5 and the sum of a does not exceed 2 * 10^9.
    total_water = sum(a)
    if (total_water % n != 0) :
        return 'No'
        #The program returns the string 'No'
    #State: *`n` is a positive integer, `a` is a list of non-negative integers, `total_water` is the sum of `a` which is divisible by `n`, and 1 <= `n` <= 2 * 10^5 and the sum of `a` does not exceed 2 * 10^9. Additionally, `total_water` is divisible by `n`
    target = total_water // n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'No'
        
    #State: `n` is a positive integer, `a` is a list of non-negative integers, `total_water` is the sum of `a` which is divisible by `n`, `target` is an integer equal to `total_water` divided by `n`, and `container` is the sum of all elements in `a` minus `n` times `target`.
    return 'Yes'
    #The program returns the string 'Yes'.

#Overall this is what the function does:Determines whether it is possible to distribute water among containers evenly.

