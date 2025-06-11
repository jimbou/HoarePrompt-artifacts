#State of the program right berfore the function call: a and b are positive integers.
    while b:
        a, b = b, a % b
        
    #State: a is the greatest common divisor (GCD) of the initial values of a and b, and b is 0.
    return a
    #The program returns the greatest common divisor (GCD) of the initial values of a and b.

#Overall this is what the function does:Calculates and returns the greatest common divisor (GCD) of two positive integers, leaving the input variables modified in the process.

#State of the program right berfore the function call: n and m are positive integers.
    cnt = -1
    for i in range(1, m + 1):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + math.ceil(x / y) + (x % y == 0)
        
    #State: `n` and `m` are unchanged, `cnt` is at least `-1 + m`.
    return cnt
    #The program returns cnt which is at least -1 + m.

#Overall this is what the function does:This function calculates and returns a count value based on the input positive integers `n` and `m`. The count is calculated by iterating over a range from 1 to `m` (inclusive), performing arithmetic operations involving `n` and the current iteration number `i`, and incrementing the count based on the results of these operations. The function does not modify the input values `n` and `m`. The returned count is at least `-1 + m`.

