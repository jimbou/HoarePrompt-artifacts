#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 100) followed by t lines, each containing two integers n and m (1 <= n, m <= 100).
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        q = b, c
        
        if b == c:
            print('YES')
        elif b < c:
            print('NO')
        elif b % 2 == c % 2:
            print('Yes')
        else:
            print('No')
        
    #State: Output State: The loop will execute 'a' times, where 'a' is an integer between 1 and 100 (inclusive). In each iteration, it will read a line from stdin, parse it into two integers 'b' and 'c', and print 'YES' if 'b' equals 'c', 'NO' if 'b' is less than 'c', 'Yes' if 'b' and 'c' have the same parity, and 'No' otherwise. After 'a' iterations, the loop will terminate, and the state of 'a' will be unchanged, but 'a' lines will have been read from stdin and 'a' lines will have been printed to stdout.

#Overall this is what the function does:This function reads a series of integer pairs from standard input, compares each pair, and prints a corresponding result based on their values and parity. It iterates this process a number of times specified by the first input integer, producing a series of 'YES', 'NO', 'Yes', or 'No' outputs.

