#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the length of the array) and then a space-separated list of integers. The length of the list is equal to the first integer. The integers are between 1 and 10^9.
    """Median of Array"""
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        p = (n + 1) // 2 - 1
        
        res = a.count(a[p])
        
        print(res)
        
    #State: The number of occurrences of the median of the list of integers in each test case, printed on a new line for each test case.

#Overall this is what the function does:Reads multiple test cases from standard input, where each test case consists of an integer (array length) followed by a space-separated list of integers. For each test case, it sorts the list, finds the median, counts the occurrences of the median, and prints the count on a new line.

