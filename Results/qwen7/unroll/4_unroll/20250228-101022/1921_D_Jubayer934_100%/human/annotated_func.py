#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100. For each test case, n and m are integers satisfying 1 ≤ n ≤ m ≤ 2 ⋅ 10^5, and the sum of m over all test cases does not exceed 2 ⋅ 10^5. a_i and b_i are lists of integers where 1 ≤ a_i, b_i ≤ 10^9 for all i.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        temp = -1
        
        ans = []
        
        a = sorted(map(int, input().split()))[:n]
        
        b = sorted(map(int, input().split()), reverse=True)[:m]
        
        for i in range(n):
            if abs(a[i] - b[-(n - i)]) > abs(a[i] - b[i]):
                temp = i
                break
            ans.append(abs(a[i] - b[i]))
        
        if temp != -1:
            for i in range(temp, n):
                ans.append(abs(a[i] - b[-(n - i)]))
        
        print(sum(ans))
        
    #State: Output State: The sum of absolute differences between the first n smallest elements of list a and the first m largest elements of list b, after processing all test cases according to the given logic.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads integers n and m, along with two lists a and b. It then sorts list a in ascending order and list b in descending order. The function calculates the sum of absolute differences between the first n smallest elements of list a and the first m largest elements of list b. If a certain condition is met during the calculation, it adjusts the result accordingly. Finally, it prints the computed sum for each test case.

