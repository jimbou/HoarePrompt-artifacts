#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t sets of three integers a, b, and m (1 <= a, b, m <= 10^18).
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        print(m // a + m // b + 2)
        
    #State: The output state will be the sum of the quotients of m divided by a and m divided by b, plus 2, for each set of three integers a, b, and m, repeated t times.

#Overall this is what the function does:The function reads an integer t from standard input, representing the number of test cases. For each test case, it reads three integers a, b, and m, and prints the sum of the quotients of m divided by a and m divided by b, plus 2. This process is repeated t times, resulting in t outputs.

