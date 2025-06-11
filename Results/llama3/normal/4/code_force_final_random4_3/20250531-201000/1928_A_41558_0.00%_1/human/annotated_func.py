#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains a single integer t (1 <= t <= 10^4). Each of the following t lines contains two integers a and b (1 <= a, b <= 10^9).
    n = int(input())
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 != 0 and b % 2 != 0:
            print('NO')
        elif a / 2 == b or b / 2 == a:
            print('NO')
        else:
            print('YES')
        
    #State: `n` is an integer between 0 and 10^4 (inclusive), `i` is `n`, `a` and `b` are integers between 1 and 10^9 (inclusive) and are the values of the last line of input, stdin is empty. If both `a` and `b` are odd, then 'NO' is printed. If `a` is twice `b` or `b` is twice `a`, then 'NO' is printed. Otherwise, 'YES' is printed.

#Overall this is what the function does:This function reads a series of input lines from stdin, where the first line contains an integer t representing the number of test cases, and each subsequent line contains two integers a and b. It then checks each pair of integers and prints 'YES' if the pair meets certain conditions (i.e., not both odd, and not one being twice the other), and 'NO' otherwise. The function processes all test cases and prints the corresponding results, leaving stdin empty after execution.

