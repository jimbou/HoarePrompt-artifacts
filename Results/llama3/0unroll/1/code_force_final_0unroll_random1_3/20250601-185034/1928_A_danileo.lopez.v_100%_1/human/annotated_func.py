#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 10^4). Each of the following t lines contains two integers a and b (1 <= a, b <= 10^9).
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
        
    #State: The output state will be a series of 'Yes' or 'No' printed to the console, one for each pair of input integers (a, b). The output will be 'Yes' if either a or b is even and the other number is equal to half of the even number. Otherwise, the output will be 'No'. The value of t will remain unchanged, and the input lines from stdin will be consumed by the loop.

#Overall this is what the function does:The function reads a series of pairs of integers from standard input, where the first integer represents the number of pairs to follow. For each pair, it checks if either number is even and if the other number is equal to half of the even number. If this condition is met, it prints 'Yes' to the console; otherwise, it prints 'No'. The function consumes all input lines from standard input and does not modify the input values.

