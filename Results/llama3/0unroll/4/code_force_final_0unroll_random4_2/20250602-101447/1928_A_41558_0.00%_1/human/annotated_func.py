#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing two integers a and b (1 <= a, b <= 10^9).
    n = int(input())
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 != 0 and b % 2 != 0:
            print('NO')
        elif a / 2 == b or b / 2 == a:
            print('NO')
        else:
            print('YES')
        
    #State: The program will print 'YES' or 'NO' for each pair of integers (a, b) in the input, indicating whether the pair satisfies the conditions or not. The value of n remains unchanged.

#Overall this is what the function does:This function reads an integer t from standard input, representing the number of test cases, followed by t lines each containing two integers a and b. It then evaluates each pair (a, b) based on two conditions: (1) if both a and b are odd, or (2) if one is exactly twice the other. If either condition is met, it prints 'NO'; otherwise, it prints 'YES'. The function does not modify the input values or retain any information after execution, solely providing a yes/no assessment for each input pair.

