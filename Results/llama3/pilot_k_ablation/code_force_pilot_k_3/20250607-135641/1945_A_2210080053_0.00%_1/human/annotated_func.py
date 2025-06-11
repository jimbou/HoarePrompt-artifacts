#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three space-separated integers a, b, and c, where a, b, and c are non-negative integers.
    for line in [*open(0)][1:]:
        p, q, r = map(int, line.split())
        
        q += r
        
        print((p - q // 3, -1)[r < q % 3])
        
    #State: p is an integer, q is an integer equal to its original value plus the number of test cases times the value of r, r is an integer, stdin contains no test cases, open(0) has no lines, and this is printed: a tuple containing the difference between p and the integer division of q by 3 if r is greater than or equal to the remainder of q divided by 3, otherwise -1

#Overall this is what the function does:The function processes multiple test cases from standard input, where each test case contains three space-separated integers a, b, and c. It calculates the sum of b and c, then prints a tuple containing the difference between a and the integer division of the sum by 3 if c is greater than or equal to the remainder of the sum divided by 3, otherwise it prints -1. After processing all test cases, the function leaves the standard input empty and the file object open(0) with no lines.

