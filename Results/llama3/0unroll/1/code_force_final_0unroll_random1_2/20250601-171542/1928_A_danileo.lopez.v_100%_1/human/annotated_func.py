#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^4) followed by t lines, each containing two integers a and b (1 <= a, b <= 10^9).
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
        
    #State: The output will be a series of 'Yes' or 'No' for each pair of input integers (a, b), indicating whether a can be transformed into b or vice versa by repeatedly dividing by 2, with the condition that at least one of a or b is even. The number of lines in the output will be equal to the value of t. The value of t and the input lines will remain unchanged.

#Overall this is what the function does:Determines whether two given integers can be transformed into each other by repeatedly dividing by 2, with the condition that at least one of the integers is even, and outputs 'Yes' or 'No' accordingly for each pair of input integers.

