#State of the program right berfore the function call: stdin contains multiple test cases. The first line contains a single integer t (1 <= t <= 10^3). Each test case contains a single integer n (3 <= n <= 10^5).
    for _ in range(int(input())):
        n = int(input())
        
        a = list(range(1, n + 1))
        
        for i in range(n // 2):
            a[2 * i + 1] = n - i
            a[2 * i] = i + 1
        
        if len(a) % 2 == 1:
            a[n - 1] = n // 2 + 1
        
        print(*a)
        
    #State: stdin is empty, t is an integer between 1 and 10^3, n is an integer between 3 and 10^5, a is a list of integers where a[2 * i] = i + 1 and a[2 * i + 1] = n - i for i in range(n // 2). If the length of a is odd, a[n - 1] = n // 2 + 1. The elements of the list a have been printed t times.

#Overall this is what the function does:Reads multiple test cases from standard input, where each test case contains a single integer n, and prints a rearranged list of integers from 1 to n, with the first and second halves of the list swapped and the middle element adjusted if the length of the list is odd, repeating this process for each test case.

