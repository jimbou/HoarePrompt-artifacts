#State of the program right berfore the function call: stdin contains multiple lines of input. The first line contains an integer t (1 <= t <= 100). Each of the following t lines contains two integers n and m (1 <= n, m <= 100).
    a = int(input())
    for i in range(a):
        b, c = map(int, input().split())
        
        q = b, c
        
        if b == c:
            print('YES')
        elif b < c:
            print('NO')
        elif a % 2 == b % 2:
            print('Yes')
        else:
            print('No')
        
    #State: Output State: The output state is a series of 'YES', 'NO', 'Yes', or 'No' printed to the console, depending on the values of b and c read from stdin in each iteration of the loop. The number of lines printed is equal to the value of a. The value of a remains unchanged.

#Overall this is what the function does:The function reads a series of input lines from stdin, where the first line contains an integer t, and each subsequent line contains two integers n and m. It then prints a series of 'YES', 'NO', 'Yes', or 'No' to the console, depending on the values of n and m, for a total of t lines. The function does not modify the input values or store any results, only printing the output state to the console.

