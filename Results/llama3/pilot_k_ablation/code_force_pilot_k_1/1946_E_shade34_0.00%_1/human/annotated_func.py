#State of the program right berfore the function call: a and b are integers and b is non-zero.
    if (b == 0) :
        return 1, 0
        #The program returns two values: 1 and 0. The value 1 is an integer and the value 0 is also an integer and is equal to the initial value of variable b.
    #State: a and b are integers and b is non-zero, and b is not equal to 0
    if (a < b) :
        c, d = func_1(b, a)
        return d, c
        #The program returns two values: `d` and `c`, which are the return values of `func_1(b, a)`, where `a` is an integer less than `b`, and `b` is a non-zero integer.
    #State: a and b are integers, b is non-zero, and a is not less than b
    if (a % b == 0) :
        return 1, -(a // b - 1)
        #The program returns two values: 1 and the negation of the difference between the quotient of a divided by b and 1. Since a is a multiple of b, the quotient a // b is an integer. The difference between this quotient and 1 is then negated, resulting in a negative integer or zero.
    #State: *a and b are integers, b is non-zero, a is not less than b, and a is not divisible by b
    c, d = func_1(b, a % b)
    return d, c - a // b * d
    #The program returns a tuple containing two values. The first value is `d`, which is the return value of `func_1(b, a % b)`. The second value is the result of the expression `c - a // b * d`, where `c` is also a return value of `func_1(b, a % b)`, `a` is an integer not less than `b` and not divisible by `b`, and `b` is a non-zero integer.

#Overall this is what the function does:This function takes two integers, a and b, as input, where b is non-zero. It returns a tuple of two values. If b is zero, it returns (1, 0). If a is less than b, it calls another function, func_1, with b and a as arguments and returns the result. If a is a multiple of b, it returns (1, -((a // b) - 1)). Otherwise, it calls func_1 with b and the remainder of a divided by b as arguments, and returns a tuple containing the first return value of func_1 and the result of subtracting the product of the second return value of func_1, a, and b from the first return value of func_1.

#State of the program right berfore the function call: a and b are non-negative integers, a and b are the result of a previous computation and are used to compute the final result modulo 10^9 + 7.
    c, d = func_1(b, 1000000007)
    return c * a % 1000000007
    #The program returns the product of a non-negative integer 'a' and 'c' (which is the result of func_1(b, 1000000007)) modulo 1000000007.

#Overall this is what the function does:This function takes two non-negative integers 'a' and 'b' as input, computes the product of 'a' and the result of func_1(b, 1000000007), and returns the result modulo 1000000007.

