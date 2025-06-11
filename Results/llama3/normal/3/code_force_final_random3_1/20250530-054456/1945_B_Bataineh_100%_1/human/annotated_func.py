#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t sets of three space-separated integers a, b, m (1 <= a, b, m <= 10^18).
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a and m < b:
            print(2)
        elif m < a and m > b:
            print(2 + m // b)
        elif m < b and m > a:
            print(2 + m // a)
        else:
            print(m // a + m // b + 2)
        
    #State: `t` is 0, `i` is `t`, `a` is an integer between 1 and 10^18, `b` is an integer between 1 and 10^18, `m` is an integer between 1 and 10^18, stdin is empty.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of three integers a, b, and m. It then calculates and prints the minimum number of operations required to make a and b greater than or equal to m, considering the cases where m is less than a, b, or both, and where m is greater than or equal to a or b. The function processes all test cases and leaves the input stream empty.

