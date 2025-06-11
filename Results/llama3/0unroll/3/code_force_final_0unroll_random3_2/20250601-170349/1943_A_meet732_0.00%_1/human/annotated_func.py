#State of the program right berfore the function call: stdin contains multiple test cases. The first line of stdin contains a single integer t (1 <= t <= 2 * 10^4) — the number of test cases. Each test case contains two lines. The first line of each test case contains a single integer n (1 <= n <= 2 * 10^5). The second line of each test case contains n integers a_1, a_2, …, a_n (0 <= a_i < n).
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        cntl = [(0) for _ in range(n + 1)]
        
        for i in a:
            cntl[i] += 1
        
        if cntl[0] == 0:
            print(0)
        else:
            c = min(2, cntl[0])
            for j in range(1, n + 1):
                if cntl[j] < 2:
                    c -= 1
                    if not c or j == n:
                        print(j)
                        break
        
    #State: The output state will contain t number of lines, each containing a single integer. This integer represents the minimum number of operations required to make all elements in the array a_i equal to 0, or -1 if it's impossible to do so.

#Overall this is what the function does:This function reads multiple test cases from standard input, where each test case consists of an array of integers. It calculates and prints the minimum number of operations required to make all elements in the array equal to 0, or -1 if it's impossible to do so. The function iterates through each test case, counting the occurrences of each integer in the array, and then determines the minimum number of operations needed to reduce all elements to 0. If it's impossible to make all elements equal to 0, the function prints -1. Otherwise, it prints the minimum number of operations required.

