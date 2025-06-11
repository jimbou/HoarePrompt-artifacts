#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the length of the array) and then a space-separated list of integers (the array). The length of the array is a non-negative integer and the integers in the array are between 1 and 10^9.
    """Median of Array"""
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        p = (n + 1) // 2 - 1
        
        res = a.count(a[p])
        
        print(res)
        
    #State: stdin contains no test cases, t is a non-negative integer

#Overall this is what the function does:Reads multiple test cases from standard input, where each test case consists of an integer (array length) followed by a space-separated list of integers (the array). For each test case, it sorts the array, finds the median element, counts its occurrences, and prints the count. After processing all test cases, the function leaves the standard input empty.

