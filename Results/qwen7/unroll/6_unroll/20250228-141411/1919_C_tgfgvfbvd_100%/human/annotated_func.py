#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of an integer n such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ n. The sum of all n values across all test cases does not exceed 2⋅10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        a, b = float('inf'), float('inf')
        
        c = 0
        
        for x in range(n):
            if a > b:
                a, b = b, a
            if l[x] <= a:
                a = l[x]
            elif l[x] <= b:
                b = l[x]
            else:
                a = l[x]
                c += 1
        
        print(c)
        
    #State: Output State: c is the count of elements in the list l that are greater than both a and b after processing all elements in the list for each test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer n and a list of n integers. For each test case, it finds the count of elements in the list that are greater than both the current minimum (a) and the second minimum (b) values encountered so far. It then prints this count for each test case.

