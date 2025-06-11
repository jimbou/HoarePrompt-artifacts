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
        
    #State: The output state will contain multiple lines, each representing the modified list 'a' for each test case. The list 'a' will have its elements rearranged such that the first half of the list contains the numbers from 1 to n/2 in ascending order, and the second half contains the numbers from n/2 + 1 to n in descending order. If the length of the list is odd, the middle element will be n/2 + 1.

#Overall this is what the function does:Rearranges the elements of a list from 1 to n in a specific order for multiple test cases. For each test case, it takes an integer n as input, creates a list of numbers from 1 to n, and then rearranges the list such that the first half contains numbers from 1 to n/2 in ascending order, and the second half contains numbers from n/2 + 1 to n in descending order. If the length of the list is odd, the middle element is set to n/2 + 1. The modified list is then printed as output for each test case.

