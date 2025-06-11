#State of the program right berfore the function call: a and b are positive integers.
    while b:
        a, b = b, a % b
        
    #State: a is the greatest common divisor (GCD) of the initial values of a and b, and b is 0.
    return a
    #The program returns the greatest common divisor (GCD) of the initial values of a and b.

#Overall this is what the function does:This function calculates and returns the greatest common divisor (GCD) of two positive integers, modifying the input variables in the process. It takes two positive integers as input and returns their GCD, leaving one of the input variables as the GCD and the other as 0.

#State of the program right berfore the function call: n and m are positive integers such that 1 <= n, m <= 2 * 10^6.
    cnt = -1
    for i in range(1, m + 1):
        x = n - (i * i - i)
        
        y = i * i
        
        cnt = cnt + math.ceil(x / y) + (x % y == 0)
        
    #State: Output State: `cnt` is the sum of the ceiling of `(n - i^2 + i) / i^2` and a boolean value indicating whether `(n - i^2 + i)` is divisible by `i^2`, for all `i` from 1 to `m`.
    return cnt
    #The program returns the sum of the ceiling of `(n - i^2 + i) / i^2` and a boolean value indicating whether `(n - i^2 + i)` is divisible by `i^2`, for all `i` from 1 to `m`.

#Overall this is what the function does:This function calculates the sum of the ceiling of `(n - i^2 + i) / i^2` and a boolean value indicating whether `(n - i^2 + i)` is divisible by `i^2`, for all `i` from 1 to `m`, where `n` and `m` are positive integers such that 1 <= n, m <= 2 * 10^6, and returns this sum.

