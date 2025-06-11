#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for _ in range(int(input())):
        p = list(map(lambda x: int(x) - int(x) % 2, input().split()))
        
        print((sum(list(map(lambda x: x % 2 > 0, p[:3]))) == 3) + sum(p) // 2)
        
    #State: The sum of the results of each iteration, where each result is the sum of the first three elements of p divided by 2, plus 1 if the sum of the remainders of the first three elements of p divided by 2 is equal to 3.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of four integers. It then processes each test case by rounding down each integer to the nearest even number, checks if the sum of the remainders of the first three integers divided by 2 equals 3, and prints the sum of the rounded integers divided by 2 plus 1 if the condition is met, or just the sum of the rounded integers divided by 2 otherwise. The function repeats this process for each test case and does not return any value.

