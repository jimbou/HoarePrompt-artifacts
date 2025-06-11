#State of the program right berfore the function call: q and x are integers such that 1 <= x < q <= 10^9.
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: *q is an integer greater than or equal to 1 and less than or equal to 10^9, x is an integer such that 1 <= x < q, if the square root of q is an integer greater than or equal to x - 1, then M is a list containing the integer square root of q. Otherwise, M remains an empty list.
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
        i += 1
        
    #State: M contains all divisors of q that are greater than or equal to x - 1, and i is equal to w.
    return M
    #The program returns M, which contains all divisors of q that are greater than or equal to x - 1.

#Overall this is what the function does:This function takes two integers, q and x, as input, where 1 <= x < q <= 10^9, and returns a list M containing all divisors of q that are greater than or equal to x - 1. The function first checks if the square root of q is an integer greater than or equal to x - 1, and if so, adds it to the list M. Then, it iterates from 1 to the square root of q, adding any divisors of q that are greater than or equal to x - 1 to the list M. The function returns the list M, which contains all divisors of q that meet the specified condition.

