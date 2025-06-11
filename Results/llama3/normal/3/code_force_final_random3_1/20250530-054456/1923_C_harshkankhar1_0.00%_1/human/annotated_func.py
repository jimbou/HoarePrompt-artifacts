#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three inputs: first an integer, then two space-separated integers, then a space-separated list of integers, and then multiple space-separated pairs of integers. The first integer is a positive integer. The first integer in the second line is a positive integer and the second integer is a non-negative integer. The list of integers are positive integers. The pairs of integers are positive integers such that the first integer is less than or equal to the second integer and the second integer is less than or equal to the length of the list of integers.
    n, q = map(int, input().split())
    a = [0] + [int(x) for x in input().split()]
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        x = 1 if a[i] > 1 else 2
        
        b[i] = b[i - 1] + x
        
    #State: n is a positive integer, q is a positive integer, a is a list of n+1 positive integers where the first element is 0, b is a list of n+1 integers where the first element is 0, and for all i from 2 to n+1, the ith element of b is the (i-1)th element of b plus 1 if the ith element of a is greater than 1, otherwise it is the (i-1)th element of b plus 2.
    a = list(accumulate(a))
    print(*a)
    #This is printed: 0, 1, 3, 6, 10, 15, ... (where the list continues with the sum of the first i elements of the original list a, for i from 2 to n+1)
    for _ in range(q):
        x, y = map(int, input().split())
        
        print('NO') if a[y] - a[x - 1] < b[y] - b[x - 1] or x == y else print('YES')
        
    #State: n is a positive integer, q is 0, a is a list of n+1 positive integers where the first element is 0, and for all i from 2 to n+1, the ith element of a is the sum of the first i elements of the original list a, b is a list of n+1 integers where the first element is 0, and for all i from 2 to n+1, the ith element of b is the (i-1)th element of b plus 1 if the ith element of the original list a is greater than 1, otherwise it is the (i-1)th element of b plus 2, x is an integer, y is an integer, and either 'YES' or 'NO' is printed

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of an integer n, a positive integer q, a list of n+1 positive integers a, and q pairs of integers (x, y). It calculates the cumulative sum of the list a and prints it. Then, for each pair (x, y), it checks if the sum of the elements in the range [x, y] of the original list a is greater than or equal to the sum of the elements in the range [x, y] of the list b, which is calculated based on the values in the original list a. If the condition is met and x is not equal to y, it prints 'YES', otherwise it prints 'NO'.

