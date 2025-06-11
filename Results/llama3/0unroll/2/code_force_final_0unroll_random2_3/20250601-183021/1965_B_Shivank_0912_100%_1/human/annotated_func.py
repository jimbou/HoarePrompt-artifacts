#State of the program right berfore the function call: stdin contains an integer t (1 <= t <= 1000) followed by t lines, each containing two integers n and k (2 <= n <= 10^6, 1 <= k <= n).
    t = int(input())
    for tc in range(t):
        n, k = map(int, input().split())
        
        i = 0
        
        while 1 << i + 1 <= k:
            i = i + 1
        
        ans = [k - (1 << i), k + 1, k + 1 + (1 << i)]
        
        for j in range(20):
            if j != i:
                ans.append(1 << j)
        
        print(len(ans))
        
        print(*ans)
        
    #State: The output state will contain `t` number of lines, each containing the length of the list `ans` followed by the elements of `ans`. The list `ans` will contain the numbers from 1 to 2^20 (excluding 2^i), where i is the largest integer such that 2^i is less than or equal to `k`. The numbers will be in ascending order, with the exception of the first three numbers which will be `k - 2^i`, `k + 1`, and `k + 1 + 2^i` respectively.

#Overall this is what the function does:The function reads an integer t from standard input, representing the number of test cases. For each test case, it reads two integers n and k, and generates a list of numbers from 1 to 2^20 (excluding 2^i), where i is the largest integer such that 2^i is less than or equal to k. The list is ordered, with the first three numbers being k - 2^i, k + 1, and k + 1 + 2^i, respectively. The function then prints the length of the list followed by its elements. This process is repeated for each of the t test cases.

