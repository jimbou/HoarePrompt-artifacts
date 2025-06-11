#State of the program right berfore the function call: q and x are integers such that 1 <= x < q <= 10^9.
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: *q is an integer such that q <= 10^9, x is an integer such that 1 <= x < q, if the square root of q is an integer and is greater than or equal to x - 1, then M is a list containing the square root of q. Otherwise, M is an empty list.
    for i in range(1, int(w // 1)):
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
    #State: Output State: *q is an integer such that q <= 10^9, x is an integer such that 1 <= x < q, M is a list containing all the divisors of q that are greater than or equal to x - 1.
    return M
    #The program returns a list M containing all the divisors of an integer q that are greater than or equal to x - 1, where q is an integer such that q <= 10^9 and x is an integer such that 1 <= x < q.

#Overall this is what the function does:This function takes two integers, q and x, as input, where 1 <= x < q <= 10^9, and returns a list of all divisors of q that are greater than or equal to x - 1. The function includes the square root of q in the list if it is an integer and greater than or equal to x - 1. It also includes all other divisors of q that meet the condition, including both the divisor and the quotient if they are greater than or equal to x - 1. The function returns an empty list if no divisors meet the condition.

