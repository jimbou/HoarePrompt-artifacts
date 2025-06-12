#State of the program right berfore the function call: stdin contains two inputs: first an integer (1 <= t <= 10^3) and then t integers (3 <= n <= 10^5).
    for _ in range(int(input())):
        n = int(input())
        
        a = list(range(1, n + 1))
        
        for i in range(n // 2):
            a[2 * i + 1] = n - i
            a[2 * i] = i + 1
        
        if len(a) % 2 == 1:
            a[n - 1] = n // 2 + 1
        
        print(*a)
        
    #State: `a` is a list of positive integers where the first half of the elements are in ascending order from 1 to `n // 2` (inclusive) and the second half of the elements are in descending order from `n` to `n // 2 + 1` (inclusive). If the length of `a` is an odd number, the middle element is `n // 2 + 1`. The list `a` has been printed `t` times, where `t` is the number of test cases.

#Overall this is what the function does:This function reads a series of test cases from standard input, where each test case consists of an integer 't' followed by 't' integers 'n'. For each 'n', it generates a list 'a' of length 'n' and rearranges its elements such that the first half are in ascending order from 1 to 'n // 2' and the second half are in descending order from 'n' to 'n // 2 + 1'. If 'n' is odd, the middle element is set to 'n // 2 + 1'. The rearranged list 'a' is then printed for each test case.

