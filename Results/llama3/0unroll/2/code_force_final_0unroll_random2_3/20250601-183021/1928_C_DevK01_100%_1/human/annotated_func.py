#State of the program right berfore the function call: q and x are integers such that 1 <= x < q <= 10^9.
    M = []
    w = math.sqrt(q)
    if (w == w // 1 and w >= x - 1) :
        M += [w]
    #State: *q is an integer greater than or equal to 1 and less than or equal to 10^9, x is an integer such that 1 <= x < q, w is a float equal to the square root of q. If the square root of q is an integer and is greater than or equal to x - 1, then M is a list containing the square root of q. Otherwise, M remains an empty list.
    i = 1
    while i < w:
        if q % i == 0:
            if i >= x - 1:
                M += [i]
            if q // i >= x - 1:
                M += [q // i]
        
        i += 1
        
    #State: The loop will iterate from 1 to the square root of q (inclusive), and for each iteration i, if q is divisible by i, it will add i and q // i to the list M if they are greater than or equal to x - 1. The final state will be the list M containing all the divisors of q that are greater than or equal to x - 1 and less than or equal to the square root of q.
    return M
    #The program returns a list M containing all the divisors of q that are greater than or equal to x - 1 and less than or equal to the square root of q.

#Overall this is what the function does:This function finds and returns all divisors of a given integer q that are greater than or equal to x - 1 and less than or equal to the square root of q. It accepts two parameters, q and x, where q is an integer between 1 and 10^9 (inclusive) and x is an integer such that 1 <= x < q. The function returns a list containing these divisors.

