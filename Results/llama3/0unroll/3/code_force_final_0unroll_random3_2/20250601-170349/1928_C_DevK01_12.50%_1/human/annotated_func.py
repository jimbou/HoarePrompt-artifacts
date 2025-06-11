#State of the program right berfore the function call: q and x are integers such that 1 <= x < q <= 10^9.
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: *q is an integer greater than or equal to 1 and less than or equal to 10^9, x is an integer such that 1 <= x < q. If the square root of q is an integer and is greater than or equal to x - 1, then M is a list containing the square root of q. Otherwise, M remains an empty list.
    for i in range(1, int(w // 1)):
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
    #State: Output State: *q is an integer greater than or equal to 1 and less than or equal to 10^9, x is an integer such that 1 <= x < q. M is a list containing all the divisors of q that are greater than or equal to x - 1.
    return M
    #The program returns a list M containing all the divisors of q that are greater than or equal to x - 1, where q is an integer greater than or equal to 1 and less than or equal to 10^9, and x is an integer such that 1 <= x < q.

#Overall this is what the function does:This function takes two integers, q and x, as input, where 1 <= x < q <= 10^9, and returns a list M containing all the divisors of q that are greater than or equal to x - 1. The function identifies divisors by checking all numbers from 1 to the square root of q, and includes both the divisor and its corresponding quotient if they meet the condition. The function returns an empty list if no such divisors are found.

