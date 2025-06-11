#State of the program right berfore the function call: n is a positive integer, a is a list of non-negative integers, the sum of a is divisible by n, and 1 <= n <= 2 * 10^5 and the sum of a does not exceed 2 * 10^9.
    total_water = sum(a)
    target = total_water // n
    if (total_water % n != 0) :
        return 'NO'
        #The program returns the string 'NO'.
    #State: *n is a positive integer, a is a list of non-negative integers, total_water is the sum of a, target is the integer division of total_water by n, and total_water is divisible by n
    container = 0
    for water in a:
        container += water - target
        
        if container < 0:
            return 'NO'
        
    #State: `n` is a positive integer, `a` is a list of non-negative integers with at least `n` elements, `total_water` is the sum of `a`, `target` is the integer division of `total_water` by `n`, `container` is the sum of the elements in `a` minus `n` times the integer division of the sum of `a` by `n`, and `water` is the last element in `a`. If `container` is less than 0, the program returns the string 'NO'. Otherwise, no specific action is taken.
    return 'YES'
    #The program returns the string 'YES'.

#Overall this is what the function does:This function determines whether it is possible to distribute a certain amount of water into n containers, where the total amount of water is divisible by n. It takes two inputs: a positive integer n and a list of non-negative integers a representing the amount of water in each container. The function returns 'YES' if the water can be distributed evenly among the containers and 'NO' otherwise. If the total amount of water is not divisible by n, the function immediately returns 'NO'. Otherwise, it iterates through the list of water amounts, calculating the target amount for each container and checking if the current container can hold the target amount. If at any point a container cannot hold the target amount, the function returns 'NO'. If the function completes the iteration without returning 'NO', it returns 'YES', indicating that the water can be distributed evenly among the containers.

