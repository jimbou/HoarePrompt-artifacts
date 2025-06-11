#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three integers t, k, and x (1 <= t <= 10^4, 1 <= k,x <= t). The second line contains t integers a_1, a_2,...,a_t (1 <= a_i <= 1000).
    for _ in range(int(input())):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        a.reverse()
        
        sum1 = sum(a)
        
        ans = []
        
        for i in range(k + 1):
            if i == 0:
                sums = sum1 - 2 * sum(a[:x + 1])
                ans.append(sums)
            elif i + x - 1 < n:
                sums = sums + a[i - 1] - 2 * a[i + x - 1]
                ans.append(sums)
            else:
                sums = sums + a[i - 1]
                ans.append(sums)
        
        print(max(ans))
        
    #State: n, k, x are integers, a is a list of integers in descending order, sum1 is the sum of the integers in a, stdin is empty, i is equal to the value of t, ans is a list containing the maximum sum of the integers in a excluding the first x+1 integers multiplied by 2, and the maximum value in the list ans is printed

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers: the number of elements (n), a value (k), and another value (x). The second line contains n integers. The function sorts these integers in descending order, calculates the sum of all integers, and then iterates k+1 times to calculate a new sum by subtracting twice the value of the xth integer and adding the value of the previous integer. The function prints the maximum sum calculated during these iterations. The function repeats this process for all test cases until standard input is empty.

