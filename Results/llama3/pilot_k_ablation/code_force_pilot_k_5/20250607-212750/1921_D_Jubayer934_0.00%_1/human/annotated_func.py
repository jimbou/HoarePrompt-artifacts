#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains three lines. The first line contains two integers n and m (1 ≤ n ≤ m ≤ 2⋅10^5). The second line contains n integers a_i (1 ≤ a_i ≤ 10^9). The third line contains m integers b_i (1 ≤ b_i ≤ 10^9).
    n = int(input())
    for i in range(n):
        m, n = map(int, input().split())
        
        a = list(map(int, input().split()))[:m]
        
        b = list(map(int, input().split()))[:n]
        
        b.sort()
        
        result = []
        
        n = n // 2
        
        for i in range(len(a)):
            if len(a) == len(b):
                break
            b.remove(b[n - 1])
        
        for i in range(len(a)):
            result.append(abs(max(a) - min(b)))
            a.remove(max(a))
            b.remove(min(b))
        
        print(sum(result))
        
    #State: n is 0, i is equal to the original value of n, m is an integer, a is an empty list, b is a sorted list of n integers, result is a list containing n integers, each integer is the absolute difference between the maximum value in the updated list a and the minimum value in the updated list b, and the sum of result is printed.

#Overall this is what the function does:This function processes multiple test cases from standard input, where each test case contains two lists of integers. It calculates the absolute differences between the maximum values of the first list and the minimum values of the second list, after removing elements from the second list to make it the same length as the first list. The function then prints the sum of these absolute differences for each test case.

