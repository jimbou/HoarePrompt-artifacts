#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two inputs: first an integer (the length of the array) and then a space-separated list of integers (the array). The length of the array is a positive integer and does not exceed 10^5. The integers in the array are positive and do not exceed 10^9.
    """Median of Array"""
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        p = (n + 1) // 2 - 1
        
        res = a.count(a[p])
        
        print(res)
        
    #State: t is 0, _ is t, n is an integer, a is a sorted list of integers, p is an integer, res is an integer equal to the count of the middle element in the sorted list a, and stdin contains multiple test cases minus t, and the count of the middle element in the sorted list a which is equal to res is being printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an integer (array length) and a space-separated list of integers (the array). It sorts each array, finds the middle element, counts its occurrences, and prints the count. The function processes all test cases and prints the count of the middle element for each array.

