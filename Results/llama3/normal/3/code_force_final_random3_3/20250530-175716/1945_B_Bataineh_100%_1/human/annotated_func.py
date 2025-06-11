#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, and m (1 <= a, b, m <= 10^18).
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
        
    #State: `t` is an integer greater than or equal to 0, `i` is `t`, `a`, `b`, and `m` are integers assigned from the input, stdin is empty. If `m` is less than both `a` and `b`, the number 2 is printed. If `m` is less than `a` and greater than `b`, the program prints 2 plus the integer division of `m` by `b`. If `m` is between `a` and `b` (exclusive), the program prints 2 plus the integer division of `m` by `a`. Otherwise, the program prints the sum of the integer divisions of `m` by `a` and `b`, plus 2.

#Overall this is what the function does:The function reads a series of test cases from standard input, where each case consists of three integers a, b, and m. It then calculates and prints the minimum number of operations required to make both a and b greater than or equal to m. The operations considered are adding a or b to themselves, and the function prints the result for each test case. The function does not return any value, but instead prints the results directly to standard output.

