#State of the program right berfore the function call: q and x are integers such that 1 <= x < q <= 10^9.
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: *q is an integer greater than or equal to 1 and less than or equal to 10^9, x is an integer greater than or equal to 1 and less than q. If the square root of q is an integer and is greater than or equal to x - 1, then M is a list containing the square root of q. Otherwise, M remains an empty list.
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
        i += 1
        
    #State: `q` is an integer greater than or equal to 1 and less than or equal to 10^9, `x` is an integer greater than or equal to 1 and less than `q`, `i` is equal to `w`, `w` is greater than or equal to 1. If the square root of `q` is an integer and is greater than or equal to `x` - 1, then `M` is a list containing the square root of `q`. Otherwise, `M` is a list containing all integers `i` such that `i` is greater than or equal to `x` - 1 and `q` is divisible by `i`.
    return M
    #The program returns a list M. If the square root of q is an integer and is greater than or equal to x - 1, then M contains the square root of q, which is an integer greater than or equal to 1 and less than or equal to the square root of 10^9. Otherwise, M contains all integers i such that i is greater than or equal to x - 1 (where x is an integer greater than or equal to 1 and less than q) and q is divisible by i.

#Overall this is what the function does:This function takes two integers, q and x, as input, where 1 <= x < q <= 10^9, and returns a list M containing divisors of q that are greater than or equal to x - 1. If the square root of q is an integer and is greater than or equal to x - 1, the list contains only the square root of q. Otherwise, the list contains all integers i such that i is greater than or equal to x - 1 and q is divisible by i.

