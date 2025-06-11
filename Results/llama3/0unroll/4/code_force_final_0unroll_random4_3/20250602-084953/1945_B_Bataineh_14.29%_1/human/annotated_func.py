#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing three integers a, b, and m (1 <= a, b, m <= 10^18).
    t = int(input())
    for i in range(t):
        a, b, m = map(int, input().split())
        
        if m < a or m < b:
            print(2)
        else:
            print(m // a + m // b + 2)
        
    #State: The output will be a series of integers, each representing the minimum number of operations required to make a and b equal to m. If m is less than either a or b, the output will be 2. Otherwise, the output will be the sum of the integer divisions of m by a and b, plus 2. The number of output lines will be equal to the value of t.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of three integers a, b, and m. It calculates and prints the minimum number of operations required to make a and b equal to m. If m is less than either a or b, it outputs 2. Otherwise, it outputs the sum of the integer divisions of m by a and b, plus 2. The function processes multiple test cases and prints the result for each case.

