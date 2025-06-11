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
        
    #State: n is an integer, a is a list of integers where the value at index 2*i+1 is n-i, the value at index 2*i is i+1, and the rest of the values are from 1 to n. If the length of a is odd, the value at index n-1 is n//2 + 1., and the list a is printed.

#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case is an integer n. It then rearranges the numbers from 1 to n in a specific pattern, where the value at index 2*i+1 is n-i and the value at index 2*i is i+1. If the length of the list is odd, the value at index n-1 is set to n//2 + 1. Finally, it prints the rearranged list for each test case.

