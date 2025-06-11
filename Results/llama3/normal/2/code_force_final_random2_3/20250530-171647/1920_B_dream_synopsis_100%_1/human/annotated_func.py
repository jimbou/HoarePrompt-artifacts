#State of the program right berfore the function call: stdin contains multiple test cases. Each test case contains two lines. The first line contains three integers t, k, and x (1 ≤ t ≤ 10^4, 1 ≤ k,x ≤ t). The second line contains t integers a_1, a_2,...,a_t (1 ≤ a_i ≤ 1000).
    for _ in range(int(input())):
        n, k, x = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        a.reverse()
        
        sum1 = sum(a)
        
        ans = []
        
        for i in range(k + 1):
            if i == 0:
                sums = sum1 - 2 * sum(a[:x])
                ans.append(sums)
            elif i + x - 1 < n:
                sums = sums + a[i - 1] - 2 * a[i + x - 1]
                ans.append(sums)
            else:
                sums = sums + a[i - 1]
                ans.append(sums)
        
        print(max(ans))
        
    #State: n is an integer, k is an integer greater than or equal to 0, x is an integer, a is a list of integers in descending order, sum1 is the sum of all integers in a, ans is a list containing the updated value of sums, i is equal to k, sums is the sum of all integers in a minus 2 times the sum of the first x integers in a plus the sum of the integers from index x to k-1 minus 2 times the sum of the integers from index 2*x-1 to k+x-2 if k+x-1 is less than n. Otherwise, sums is the sum of all integers in a plus the sum of the integers from index x to k-1 if k+x-1 is not less than n, and the maximum value in the ans list is printed, and stdin contains multiple test cases minus 2 inputs.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of two lines. The first line contains three integers: the number of elements (t), an integer k, and an integer x. The second line contains t integers. The function sorts these integers in descending order, calculates a series of sums by subtracting twice the sum of the first x integers and adding the sum of the next k-1 integers, and stores these sums in a list. It then prints the maximum sum from this list. The function repeats this process for all test cases in the input.

