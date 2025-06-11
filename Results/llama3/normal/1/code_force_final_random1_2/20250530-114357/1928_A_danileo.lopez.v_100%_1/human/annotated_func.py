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
        
    #State: `_` is `t`, `t` is an integer between 1 and 10^4 (inclusive), `a` and `b` are integers between 1 and 10^9 (inclusive).

#Overall this is what the function does:This function reads an integer t from standard input, representing the number of test cases, followed by t lines, each containing two integers a and b. It then checks each pair of integers to determine if they can be divided evenly into two equal parts, either by dividing a or b by 2. If either a or b can be divided evenly into two equal parts and the resulting part is equal to the other number, it prints 'Yes'. Otherwise, it prints 'No'. The function does not return any value, but rather prints the results directly to standard output.

