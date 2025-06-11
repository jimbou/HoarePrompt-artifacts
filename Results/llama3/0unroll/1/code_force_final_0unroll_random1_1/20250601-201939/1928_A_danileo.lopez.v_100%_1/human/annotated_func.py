#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 ≤ t ≤ 10^4). Each of the following t lines contains two integers a and b (1 ≤ a, b ≤ 10^9).
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        
        if a % 2 == 0 or b % 2 == 0:
            if a % 2 == 0:
                a1, a2 = a // 2, a // 2
                if a1 != b:
                    print('Yes')
                    continue
            if b % 2 == 0:
                b1, b2 = b // 2, b // 2
                if b1 != a:
                    print('Yes')
                    continue
            print('No')
        else:
            print('No')
        
    #State: The output state will contain t lines, each with either 'Yes' or 'No'. For each line, if the corresponding input values a and b are both odd, the output will be 'No'. If either a or b is even, the output will be 'Yes' if the other number is equal to half of the even number, and 'No' otherwise.

#Overall this is what the function does:This function reads input from stdin, processes multiple pairs of integers, and outputs 'Yes' or 'No' for each pair based on specific conditions. It checks if either number in a pair is even and if the other number is equal to half of the even number, printing 'Yes' if the condition is met and 'No' otherwise. If both numbers in a pair are odd, it prints 'No'. The function processes a specified number of pairs (t) and outputs the results accordingly.

