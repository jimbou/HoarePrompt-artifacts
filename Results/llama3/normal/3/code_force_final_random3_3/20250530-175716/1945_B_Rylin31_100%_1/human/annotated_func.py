#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t sets of three space-separated integers a, b, and m (1 <= a, b, m <= 10^18).
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        print(m // a + m // b + 2)
        
    #State: `t` is an integer between 1 and 10^4 (inclusive) and is equal to 0, `i` is equal to `t`, `a` is an integer between 1 and 10^18 (inclusive), `b` is an integer between 1 and 10^18 (inclusive), `m` is an integer between 1 and 10^18 (inclusive), stdin is empty, and this is printed: m // a + m // b + 2, where m is an integer between 1 and 10^18 (inclusive), a is an integer between 1 and 10^18 (inclusive), and b is an integer between 1 and 10^18 (inclusive), for all sets of three space-separated integers a, b, and m (1 <= a, b, m <= 10^18) that were initially in stdin.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of three integers a, b, and m. It then calculates and prints the result of the expression m // a + m // b + 2 for each test case. The function continues to read and process test cases until all input has been consumed, at which point it terminates, leaving the standard input empty.

