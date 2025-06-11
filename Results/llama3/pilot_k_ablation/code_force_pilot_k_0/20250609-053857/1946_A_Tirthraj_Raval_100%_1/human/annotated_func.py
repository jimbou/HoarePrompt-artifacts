#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer n (1 <= n <= 10^5) and then n integers a_1, a_2, ..., a_n (1 <= a_i <= 10^9).
    """Median of Array"""
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        
        a = list(map(int, input().strip().split()))
        
        a.sort()
        
        p = (n + 1) // 2 - 1
        
        res = a[p:].count(a[p])
        
        print(res)
        
    #State: The loop has executed all the iterations, and the output state is the result of the last iteration. The value of 'res' is printed to the console, which represents the count of the median element in the sorted list 'a'. The other variables 'n', 'a', and 'p' have been updated with the values from the last test case. The stdin still contains the remaining test cases.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer n followed by n integers. It sorts the integers in ascending order, finds the median element, and counts the occurrences of the median element in the sorted list. The function then prints the count of the median element for each test case.

