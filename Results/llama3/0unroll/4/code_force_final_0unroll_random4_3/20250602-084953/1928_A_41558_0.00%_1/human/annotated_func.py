#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two space-separated integers a and b (1 <= a, b <= 10^9).
    n = int(input())
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 != 0 and b % 2 != 0:
            print('NO')
        elif a / 2 == b or b / 2 == a:
            print('NO')
        else:
            print('YES')
        
    #State: The output state will be a series of 'YES' or 'NO' printed to the console, each corresponding to a test case. The number of outputs will be equal to the value of `n`. The value of `n` will be unchanged, and stdin will be empty after all test cases have been processed.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two space-separated integers a and b. It then checks each test case and prints 'YES' if the numbers can be used to form a valid pair according to certain rules, and 'NO' otherwise. The rules are: if both numbers are odd, or if one number is exactly twice the other, the pair is invalid. The function processes all test cases and prints the corresponding 'YES' or 'NO' for each case, leaving the input stream empty and the number of test cases unchanged.

