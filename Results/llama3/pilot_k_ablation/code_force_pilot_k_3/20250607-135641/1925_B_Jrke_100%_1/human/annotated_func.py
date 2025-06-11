#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 10^3) followed by t lines, each containing two integers x (1 <= x <= 10^8) and n (1 <= n <= x).
    for _ in range(int(input())):
        x, n = map(int, input().split())
        
        k = x // n
        
        ans = 1
        
        for i in range(1, int(x ** 0.5) + 2):
            if x % i == 0:
                l = [ans]
                if i <= k:
                    l.append(i)
                if x // i <= k:
                    l.append(x // i)
                ans = max(l)
        
        print(ans)
        
    #State: t is 0, x is an integer greater than 0, n is an integer between 1 and x inclusive, k is an integer equal to the integer division of x by n, ans is the maximum value of the list l, l is a list containing the values of ans which is 1, i which is the square root of x rounded down to the nearest integer and if x divided by i is less than or equal to k, then x divided by i is added to the list l, stdin is empty, and the maximum value in the list l which is ans has been printed.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each case consists of two integers x and n. It calculates the maximum divisor of x that is less than or equal to x divided by n, and prints this value for each test case. The function continues to read and process test cases until the input is exhausted.

