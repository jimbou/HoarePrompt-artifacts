#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the length of the array a) and then a list of integers (the array a). The length of the array a is a non-negative integer and less or equal than 10^5. The integers in the array a are non-negative integers and less or equal than 10^9.
    """Median of Array"""
    t = int(input())
    for _ in range(t):
        n = int(input().strip())
        
        a = list(map(int, input().strip().split()))
        
        a.sort()
        
        p = (n + 1) // 2 - 1
        
        res = a[p:].count(a[p])
        
        print(res)
        
    #State: t is an integer greater than or equal to 0, _ is t-1, n is an integer, a is a sorted list of integers, p is an integer, res is an integer.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (the length of the array) followed by a list of integers. It sorts each array, finds the median value, and counts the number of occurrences of the median value. The function then prints the count of median value occurrences for each test case.

