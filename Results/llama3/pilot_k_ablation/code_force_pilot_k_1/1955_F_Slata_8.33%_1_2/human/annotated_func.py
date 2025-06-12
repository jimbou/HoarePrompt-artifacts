#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing four integers p_i (0 <= p_i <= 200).
    for i in range(int(input())):
        a, b, c, d = map(int, input().split())
        
        print(a // 2 + b // 2 + c // 2 + d // 2 + int(a % 2 + b % 2 + c % 3 == 3))
        
    #State: stdin is empty, a, b, c, d are not defined, input() returns an empty string, and the sum of the integer division of a, b, c, d by 2, plus 1 if the sum of the remainder of a, b, c divided by 2 is equal to 3, otherwise 0 has been printed t times.

#Overall this is what the function does:Reads a series of test cases from standard input, where each test case consists of four integers. For each test case, it calculates and prints the sum of the integer division of the four numbers by 2, plus 1 if the sum of the remainders of the first three numbers divided by 2 is equal to 3, otherwise 0. The function continues this process until all test cases have been read and processed, leaving the standard input empty.

